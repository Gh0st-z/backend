from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer

@api_view(['GET'])
def RegisterViewGet(request, *args, **kwargs):
    email = request.GET.get('email', None)
    user = User.objects.filter(email=email)

    if user.exists():
        return JsonResponse({'exists': True})
    else:
        return JsonResponse({'exists': False})


@api_view(['POST'])
def RegisterViewPost( request, *args, **kwargs):
    data = {
        'first_name': request.data.get('first_name'),
        'middle_name': request.data.get('middle_name'),
        'last_name': request.data.get('last_name'),
        'email': request.data.get('email'),
        'phone_number': request.data.get('phone_number'),
        'password': request.data.get('password'),
        'role': request.data.get('role'),
    }
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    return Response({'message': 'Invalid data provided!'} ,status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def LoginViewPost(request, *args, **kwargs):
    data = {
        'email': request.data.get('email'),
        'password': request.data.get('password'),
    }

    try:
        user_login = User.objects.get(email=data['email'])
    except User.DoesNotExist:
        return Response({'Error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    if check_password(data['password'], user_login.password):
        user = authenticate(request, **data)
        if user is not None:
            login(request, user)
            return Response({'message': 'Login Succeeded!'}, status=status.HTTP_200_OK)

    return Response({'Error': 'Login not succeeded!'}, status=status.HTTP_401_UNAUTHORIZED)