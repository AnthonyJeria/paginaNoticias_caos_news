from django.shortcuts import render
from noticias.models import Producto
from noticias.models import Noticia


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
    context={}
    return render(request, 'noticias/registrarse.html', context)


##def registrarse(request):
#    context={'form' : UsusarioForm()}
#    if request.method=='POST':
#        formulario=UsusarioForm(request.POST, files=request.FILES)
#
#       if formulario.is_valid:
#            formulario.save()
#            context={'mensaje':"Usuario registrado correctamente"}
#    return render(request,'noticias/registrarse.html', context)





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