from django.db import models
from django.utils import timezone
# Create your models here.



class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=3, null=False)
    created_on = models.DateTimeField(default=timezone.now)
    imagen = models.ImageField(upload_to='imagenes')
