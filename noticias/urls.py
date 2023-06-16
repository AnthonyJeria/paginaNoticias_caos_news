#from django.conf,urls import url
from django.urls import path
from . import views



urlpatterns = [
    path('index',views.index, name='index'),
    path('deportes', views.Deportes, name='deportes'),
    path('internacional', views.internacional, name='internacional'),
    path('login', views.login, name='login'),
    path('regiones', views.regiones, name='regiones'),
    path('registrarse', views.registrarse, name='registrarse'),
    path('tendencias', views.tendencias, name='tendencias'),
    path('Tienda', views.Tienda, name='Tienda'),
]