from django.contrib import admin
from .models import Categoria, Comida, Venta

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Comida)
admin.site.register(Venta)
