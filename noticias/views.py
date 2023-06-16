from django.shortcuts import render

# Create your views here.



def index(request):
    context={}
    return render(request, 'noticias/index.html', context)

def internacional(request):
    context={}
    return render(request, 'noticias/internacional.html', context)

def Deportes(request):
    context={}
    return render(request, 'noticias/Deportes.html', context)

def login(request):
    context={}
    return render(request, 'noticias/login.html', context)

def regiones(request):
    context={}
    return render(request, 'noticias/regiones.html', context)

def registrarse(request):
    context={}
    return render(request, 'noticias/registrarse.html', context)

def tendencias(request):
    context={}
    return render(request, 'noticias/tendencias.html', context)

def Tienda(request):
    context={}
    return render(request, 'noticias/Tienda.html', context)