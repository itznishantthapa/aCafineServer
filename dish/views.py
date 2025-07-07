from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Dish
from rest_framework import status
from authentication.permissions import IsSeller
from rest_framework.decorators import permission_classes
from .serializers import DishSerializer



@api_view(['GET'])
def get_dishes(request):
    dishes = Dish.objects.all()
    serializer = DishSerializer(dishes, many=True)
    return Response({'success':True,'dishes':serializer.data},status=status.HTTP_201_CREATED)




@api_view(['GET'])
def get_specific_dish(request):
    dish_id = request.query_params.get('id')

    if not dish_id:
        return Response({'error': 'Dish ID is required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        dish = Dish.objects.get(id=dish_id)
        serializer = DishSerializer(dish)
        return Response({'success':True,'dish':serializer.data}, status=status.HTTP_201_CREATED)
    except Dish.DoesNotExist:
        return Response({'error': 'Dish not found'}, status=status.HTTP_404_NOT_FOUND)




@api_view(['POST'])
# @permission_classes([IsSeller])
def create_dish(request):
    serializer = DishSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'success': True, 'dish': serializer.data}, status=status.HTTP_201_CREATED)
    else:
        return Response({'success': False, 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)




@api_view(['PUT'])
# @permission_classes([IsSeller])
def update_dish(request):
    dish_id = request.data.get('id')
    
    if not dish_id:
        return Response({'error': 'Dish ID is required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        dish = Dish.objects.get(id=dish_id)
    except Dish.DoesNotExist:
        return Response({'error': 'Dish not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = DishSerializer(dish, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({'success': True, 'dish': serializer.data})
    
    return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
# @permission_classes([IsSeller])
def delete_dish(request):
    dish_id = request.query_params.get('id')
    
    if not dish_id:
        return Response({'error': 'Dish ID is required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        dish = Dish.objects.get(id=dish_id)
        dish.delete()
        return Response({'success': True, 'message': 'Dish deleted successfully'})
    except Dish.DoesNotExist:
        return Response({'error': 'Dish not found'}, status=status.HTTP_404_NOT_FOUND)

# @api_view(['POST'])
# # @permission_classes([IsSeller])
# def update_dish_availability(request):
#     dish_id = request.data.get('id')
#     is_available = request.data.get('is_available')
    
#     if not dish_id:
#         return Response({'error': 'Dish ID is required'}, status=status.HTTP_400_BAD_REQUEST)
    
#     if is_available is None:
#         return Response({'error': 'Availability status is required'}, status=status.HTTP_400_BAD_REQUEST)

#     try:
#         dish = Dish.objects.get(id=dish_id)
#         dish.is_available = is_available
#         dish.save()
#         serializer = DishSerializer(dish)
#         return Response({'success': True, 'dish': serializer.data})
#     except Dish.DoesNotExist:
#         return Response({'error': 'Dish not found'}, status=status.HTTP_404_NOT_FOUND)
