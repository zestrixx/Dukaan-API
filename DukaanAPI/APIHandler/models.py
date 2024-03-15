from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

class Orders(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=200)
    date = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class OrderDetails(models.Model):
    order_id = models.ForeignKey(Orders, unique=True, on_delete = models.CASCADE)
    items = models.JSONField()
    customer_first_name = models.CharField(max_length=100)
    customer_last_name = models.CharField(max_length=100)
    customer_phone_number = models.IntegerField()
    address = models.CharField(max_length=200)
    landmark = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

