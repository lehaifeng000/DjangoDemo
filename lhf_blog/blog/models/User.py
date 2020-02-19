from django.db import models


class User(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20, default='123456')
    tel = models.CharField(max_length=20, null=True)



