from django.db import models
from django.contrib.auth.models import User

class Orders(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=200)
