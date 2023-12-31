from django.shortcuts import render, redirect
from noticias.models import Producto, usuario
from noticias.models import Noticia
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.db import IntegrityError


# Create your views here.



def index(request):
    noticias = Noticia.objects.order_by('fecha_noticia')[:12]
    ultimas =Noticia.objects.order_by('-fecha_noticia')[:3]
    context={
        'noticias' : noticias,
        'ultimas' : ultimas
    }
    return render(request, 'noticias/index.html', context)

def internacional(request):
    noticias = Noticia.objects.filter(id_tipo=1)
    context={
        'noticias' : noticias
    }
    return render(request, 'noticias/internacional.html', context)

def Deportes(request):
    noticias = Noticia.objects.filter(id_tipo=2)
    context={
        'noticias' : noticias
    }
    return render(request, 'noticias/Deportes.html', context)

def login(request):
    context={}
    return render(request, 'noticias/login.html', context)

def regiones(request):
    noticias = Noticia.objects.filter(id_tipo=3)
    context={
        'noticias' : noticias
        }
    return render(request, 'noticias/regiones.html', context)

def registrarse(request):
    if request.method != "POST":
        context={}
        return render(request, 'noticias/registrarse.html', context)
    else:
        if request.POST["contraseña"] == request.POST["contraseña2"]:
            try:
                obj=usuario.objects.create(nombre_completo=request.POST["nombre"],
                                           correo_electronico=request.POST["correo"],
                                           nombre_usuario=request.POST["usuario"],
                                           contrasenna=request.POST["contraseña"])
                obj.save()
                login(request, obj)
                context={'mensaje':"Usuario registrado"}
                return redirect("index")
            except IntegrityError:
                context = {"error": "El usuario ya existe"}
                return render(request, 'noticias/registrarse.html', context)
        else:
            context = {"error": "Contraseñas no coinciden"}
            return render(request, 'noticias/registrarse.html', context)

def tendencias(request):
    noticias = Noticia.objects.filter(id_tipo=4)
    context={'noticias' : noticias}
    return render(request, 'noticias/tendencias.html', context)

def Tienda(request):
    productos = Producto.objects.all()
    context={
        'productos' : productos
    }
    return render(request, 'noticias/Tienda.html', context)

def Agregar(request):
    context={}
    return render(request, 'noticias/Agregar.html', context)