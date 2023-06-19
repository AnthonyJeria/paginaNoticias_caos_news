from django.db import models

# Create your models here.

class Noticia(models.Model):
    id_noticia      =models.AutoField(db_column='idNoticia', primary_key=True)
    titular         =models.CharField(max_length=500)
    subtitulo       =models.CharField(max_length=500)
    entradilla      =models.CharField(max_length=500)
    cuerpo_noticia  =models.CharField(max_length=10000)
    fecha_noticia   =models.DateField(blank=False, null=False)
    imagen_noticia  =models.ImageField(upload_to="noticias", null=True)

    def __str__(self):
        return str(self.titular)
    
class producto(models.Model):
    id_producto     =models.AutoField(db_column='idProducto', primary_key=True)
    nombre_producto =models.CharField(max_length=50)
    precio          =models.IntegerField()
    imagen_producto  =models.ImageField(upload_to="noticias", null=True)

    def __str__(self):
        return str(self.nombre_producto)