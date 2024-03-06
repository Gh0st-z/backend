from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Pharmacy
from autho.models import User
from .serializers import PharmacySerializer

@api_view(['GET'])
def PharmacyProfileGet(request, *args, **kwargs):
    pharmacy_name = request.GET.get('pharmacy_name', None)
    pharmacy = Pharmacy.objects.filter(pharmacy_name=pharmacy_name)
    if pharmacy.exists():
        return JsonResponse({'exists': True})
    else:
        return JsonResponse({'exists': False})

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
    admin_id = request.data.get('admin_id')
    data['admin_id'] = admin_id
    serializer = PharmacySerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
