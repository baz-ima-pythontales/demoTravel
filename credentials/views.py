from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from requests import auth

from .models import Place
from .models import Team


def register(request):
    return render(request, "index1.html")


# Create your views here.
# def register(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         email = request.POST['email']
#         password = request.POST['password']
#         c_password = request.POST['c_password']
#         # if password == c_password:
#         #     if User.objects.filter(username=username).exists():
#         #         messages.info(request, "Username taken")
#         #         return redirect('register')
#         #     elif User.objects.filter(email=email).exists():
#         #         messages.info(request, "Email taken")
#         #         return redirect('register')
#         #     else:
#         #         user = User.objects.create_user(username=username, password=password, first_name=first_name,
#         #                                         last_name=last_name, email=email)
#         #         user.save();
#         # #         return redirect('login')
#         #     print("User CREATED")
#         # else:
#         #     messages.info(request, "password not matching")
#         #     return redirect('register')
#         # return redirect('/')
#     return render(request, "register.html")


# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST[' password']
#         user = auth.authenticate(username=username, password=password)
#         if user is not None:
#             auth.login(request, user)
#             return redirect('/')
#         else:
#             messages.info(request, "invalid credentials")
#             return redirect('login')
#     return render(request, 'login.html')


# def logout(request):
#     auth.logout(request)
#     return redirect('/')
