from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Dish
from rest_framework import status
from authentication.permissions import IsSeller
from rest_framework.decorators import permission_classes


@api_view(['GET'])
def get_dishes(request):
    dishes = Dish.objects.all()
    return Response(dishes)

@api_view(['POST'])
@permission_classes([IsSeller])
def create_dish(request):
    name = request.data.get('name')
    description = request.data.get('description')
    price = request.data.get('price')
    image = request.data.get('image')
    is_available = request.data.get('is_available')

    try:
        dish = Dish.objects.create(name=name, description=description, price=price, image=image, is_available=is_available)
        return Response(dish)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)