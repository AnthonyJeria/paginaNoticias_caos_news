from django.contrib import admin
from .models import Tipo_noticia, Noticia, Producto, usuario

# Register your models here.

admin.site.register(Tipo_noticia)
admin.site.register(Noticia)
admin.site.register(Producto)
admin.site.register(usuario)