from django.shortcuts import render
from .models import Productos

# Create your views here.

def ver_productos(request):
    productos = Productos.objects.all()
    return render(request, 'index.html', {'productos':productos})
