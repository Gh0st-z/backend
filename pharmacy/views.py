from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Pharmacy
from .serializers import PharmacySerializer

@api_view(['POST'])
def PharmacyProfilePost(request, *args, **kwargs):
    data = {
        'pharmacy_name': request.data.get('pharmacy_name'),
        'address': request.data.get('address'),
        'license_number': request.data.get('license_number'),
        'phone_number': request.data.get('phone_number'),
        'pharmacy_type': request.data.get('pharmacy_type'),
        'pharmacy_logo': request.data.get('pharmacy_logo'),
        'website_url': request.data.get('website_url'), 
    }
    serializer = PharmacySerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response({'message': 'Invalid data provided!'} ,status=status.HTTP_401_UNAUTHORIZED)