from tkinter import W
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from .models import AppUser as User
import json

# Create your views here.
def index(request):
    return render(request, 'todo_app/index.html')

@csrf_exempt
def signup(request):
    if request.method == 'GET':
        return render(request, 'todo_app/signup.html')

    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            User.objects.create_user(username=body['email'], email=body['email'], password=body['password'])
            return JsonResponse({'success':True})
        except Exception as e:
            print('oops!')
            print(str(e))
            return JsonResponse({'Success':False})

@csrf_exempt
def login_view(request):
    if request.method == 'GET':
        return render(request, 'todo_app/login.html')
    if request.method == 'POST':
        body = json.loads(request.body)
        email = body['email']
        password = body['password']

        user = authenticate(username=email, password=password)
        if user is not None:
            if user.is_active:
                try:
                    login(request, user)
                    print('logged in')
                    return JsonResponse({'success': True})
                except Exception as e:
                    return JsonResponse({'success': False, 'reason': 'login failed'})
            else:
                return JsonResponse({'Success': False, 'reason': 'account disabled'})
        else:
            return JsonResponse({'Success': False, 'reason': 'user does not exist'})
