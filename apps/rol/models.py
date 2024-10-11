from django.db import models

# Create your models here.
class Rol(models.Model):
    opciones=[
        ('tecnico','tecnico'),
        ('catador','catador'),
        ('barista','barista'),
        ]
    rol=models.CharField(max_length=20, choices=opciones)
    
    def __str__(self):
        return self.rol