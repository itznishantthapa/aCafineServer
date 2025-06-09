from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CustomUser
from .utils import get_tokens_for_user
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken



@api_view(['POST'])
def signup(request):
    email = request.data.get('email')
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    phone = request.data.get('phone')
    role = request.data.get('role')

    try:
        user = CustomUser.objects.get(email=email)
        is_new_user = False
    except CustomUser.DoesNotExist:
        user =CustomUser.objects.create(username=email, email=email,first_name=first_name,last_name=last_name)
        is_new_user = True
        
    tokens = get_tokens_for_user(user)
    return Response({
        'success': True, 
        'tokens': tokens,
        'isNewUser': is_new_user  # True if user was just created, False if already existed
    })



#function to get the token after expiration of the access token
@api_view(['POST'])
def refresh_token(request):
    refresh = request.data.get('refresh')
    
    if not refresh:
        return Response({'success': False, 'error': 'Refresh token is required'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        # Decode the refresh token to get the user
        refresh_token = RefreshToken(refresh)
        user = refresh_token['user_id']
        user = CustomUser.objects.get(id=user)

        
        # Generate new tokens
        tokens = get_tokens_for_user(user)
        
        return Response({'success': True, 'tokens': tokens})
    except Exception as e:
        return Response({'success': False, 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        