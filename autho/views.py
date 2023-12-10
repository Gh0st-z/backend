from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from .models import customers

@api_view(['POST'])
def login_view(request):
    if request.method == 'POST':
        data = request.POST
        email = data['email']
        passwrd = data['password']

        validating_user = customers.objects.get(email = email)
        if check_password(passwrd, validating_user.password):
            return redirect('home')