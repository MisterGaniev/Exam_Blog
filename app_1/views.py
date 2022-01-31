from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.views import View
from .models import *

# Create your views here.


class Blog(View):
    def get(self, request):
        maqola = Maqola.objects.all()
        return render(request, 'Blogs.html', {'mq' : maqola})

    def post(self, request):
        Maqola.objects.create(
            sarlavha=request.POST['title'],
            sana=request.POST['date'],
            mavzu=request.POST['theme'],
            muallif=request.POST['writer']
        )
        return redirect('blog')

def Register(request):
    if request.method == 'POST':
        x = User.objects.create_user(
            username=request.POST['name'],
            password=request.POST['password']
        )
        login(request, x)
        return redirect('login')
    return render(request, 'Registration.html')


def Login(request):
    if request.method == 'POST':
        users = authenticate(username=request.POST['login'], password=request.POST['password'])
        if users is None:
            return redirect('login')
        else:
            login(request, users)
            return redirect('blog')
    return render(request, 'Login.html')

def Logout(request):
    logout(request)
    return redirect('login')

