from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

class Orders(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=200)
    date = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.JSONField()

class OrderDetails(models.Model):
    pass