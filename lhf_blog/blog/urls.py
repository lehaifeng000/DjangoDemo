from django.urls import path

# from aaa.views import user
from .views import user

urlpatterns = [
    path('/', user.index),
    path('/login/', user.login_page),
]

