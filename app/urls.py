from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name="inicio" ),
    path('cliente/', cliente , name="cliente"),
    path('tinto/', tinto, name="tinto"),
    path('blanco/', blanco, name="blanco"),
    path('form_tinto/', formTinto, name="form_tinto"),
    path('form_tinto2/', formTinto2, name="form_tinto22"),
    path('buscar_tinto/', buscarTinto, name="buscar_tinto"),
    path('buscar2/', buscar2, name="buscar2"),
    path('buscar_blanco/', buscarBlanco, name="buscar_blanco"),
    path('buscar3/', buscar3, name="buscar3"),
    path('buscar_cliente/', buscarCliente, name="buscar_cliente"),
    path('buscar/', buscar, name="buscar"),
    path('form_blanco/', formBlanco, name="form_blanco"),
    path('form_blanco2/', formBlanco2, name="form_blanco2"),
    path('form_cliente/', formCliente, name="form_cliente"),
    path('form_cliente2/', formCliente2, name="form_cliente2"),


]  