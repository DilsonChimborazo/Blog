from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.rol.models import Rol

# Create your models here.
class User(AbstractUser):
    cedula=models.CharField(max_length=30 unique=True)
    edad=models.CharField(max_length=30 unique=True)
    rol=models.ForeignKey(Rol, on_delete=models.SET_NULL,null=True)