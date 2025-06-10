# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Order , OrderItem
from authentication.permissions import IsCustomer
from rest_framework.decorators import permission_classes
from dish.models import Dish



@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def create_order(request):
    user = request.user
    data = request.data  # expect: { "items": [{ "dish_id": 1, "quantity": 2 }, ...], "eat_mode": "EAT" }

    order = Order.objects.create(customer=user, eat_mode=data.get('eat_mode', 'EAT'),esewa_transaction_id=data.get('esewa_transaction_id'))

    for item in data['items']:
        dish = Dish.objects.get(id=item['dish_id'])
        OrderItem.objects.create(order=order, dish=dish, quantity=item['quantity'])

    return Response({'message': 'Order placed successfully', 'order_id': order.id})





@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def seller_orders(request):
    order_items = OrderItem.objects.select_related('order', 'dish').filter(
        order__is_ready=False,
        order__is_paid=False  #order__is_ready is not a typo — it’s Django ORM’s way to filter on a related model’s field.
    )
    
    result = {}
    for item in order_items:
        order_id = item.order.id
        if order_id not in result:
            result[order_id] = {
                'order_id': order_id,
                'customer_name': f"{item.order.customer.first_name} {item.order.customer.last_name}",
                'phone': item.order.customer.phone,
                'eat_mode': item.order.eat_mode,
                'order_time': item.order.order_time,
                'items': []
            }
        result[order_id]['items'].append({
            'dish_name': item.dish.name,
            'quantity': item.quantity
        })

    return Response(list(result.values()))


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def mark_order_ready(request):
    order_id = request.query_params.get('id')
    
    if not order_id:
        return Response({'error': 'Order ID is required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)

    order.is_ready = True
    order.save()

    return Response({'message': f'Order #{order_id} marked as ready'})
