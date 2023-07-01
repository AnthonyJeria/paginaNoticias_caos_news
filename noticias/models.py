from django.db import models

# Create your models here.

class Tipo_noticia(models.Model):
    id_tipo                 =models.AutoField(db_column='idTipo', primary_key=True)
    nombre_tipo_noticia     =models.CharField(max_length=50)

    def __str__(self):
        return str(self.nombre_tipo_noticia)

class Noticia(models.Model):
    id_noticia              =models.AutoField(db_column='idNoticia', primary_key=True)
    titular                 =models.CharField(max_length=500)
    subtitulo               =models.CharField(max_length=500)
    entradilla              =models.CharField(max_length=5000)
    cuerpo_noticia          =models.CharField(max_length=10000)
    fecha_noticia           =models.DateField(blank=False, null=False)
    imagen_noticia          =models.ImageField(upload_to="noticias", null=True)
    id_tipo                 =models.ForeignKey('Tipo_noticia' ,on_delete=models.CASCADE, db_column='id_tipo')
    num_subtipo_noticia     =models.IntegerField()

    def __str__(self):
        return str(self.titular)
    
class Producto(models.Model):
    id_producto     =models.AutoField(db_column='idProducto', primary_key=True)
    nombre_producto =models.CharField(max_length=50)
    precio          =models.IntegerField()
    imagen_producto  =models.ImageField(upload_to="noticias", null=True)

    def __str__(self):
        return str(self.nombre_producto)
    
class usuario(models.Model):
    id_usuario              =models.AutoField(db_column='idNoticia', primary_key=True)
    nombre_completo         =models.CharField(max_length=500)
    correo_electronico      =models.CharField(max_length=500)
    nombre_usuario          =models.CharField(max_length=500)
    contrasenna             =models.CharField(max_length=500)

    def __str__(self):
        return str(self.nombre_usuario)