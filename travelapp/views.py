from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .models import Place
from .models import Team

from . import views


# Create your views here.

def demo(request):
    obj = Place.objects.all()
    obj1 = Team.objects.all()
    result = [obj, obj1]
    return render(request, "index.html", {'result': obj, 'result1': obj1})


#
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info("Invalid")
            return redirect('login')
    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        c_password = request.POST['c_password']
        if password == c_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                                last_name=last_name, email=email)
                user.save();
                return redirect('login')
            print("User CREATED")
        else:
            messages.info(request, "password not matching")
            return redirect('register')
        return redirect('/')
    return render(request, "register.html")


def about(request):
    return render(request, "about.html")
def index(request):
    return render(request, "index.html")

