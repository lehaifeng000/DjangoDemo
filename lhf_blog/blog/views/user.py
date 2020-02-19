from django.http import HttpResponse
from ..models import User
from django.shortcuts import render


def index(request):
    return render(request, 'blog/user_index.html')


def addUser(request):
    pass


def login_page(request):
    return render(request, 'blog/user_login.html')


