from django.shortcuts import render
from django.http import HttpResponse
from .models import * 
from .forms import *

# Create your views here.

def index(request):
    return render(request, "app/base.html")

def ipa(request):
    return render(request, "app/tinto.html")

def rubia(request):
    return render(request, "app/blanco.html")


def cliente(request):
    return render(request, "app/cliente.html")


def tinto(request):
    ctx = {"db": Tinto.objects.all()}
    return render(request, "app/tinto.html", ctx)

def blanco(request):
    ctx = {"db": Blancos.objects.all()}
    return render(request, "app/blanco.html", ctx)

def cliente(request):
    ctx = {"db": Cliente.objects.all()}
    return render(request, "app/cliente.html", ctx)



def formTinto(request):
    if request.method == "POST":
        curso = Tinto(nombre=request.POST['nombre'], precio=request.POST['precio'])
        curso.save()
        return HttpResponse("Se grabó con exito")
    

    return render(request, "app/cursoForm.html")

def formTinto2(request):
     if request.method == "POST":
        miForm = formTinto(request.POST)
        if miForm.is_valid: 
             informacion = miForm.cleaned_data
             curso = Tinto(nombre=informacion['nombre'], precio=informacion['precio'])
             curso.save()
             return render(request, "app/base.html")

     else:
         miForm = Tinto()
        
        
         return render(request, "app/form_ipa2.html", {"form":miForm})

def buscarTinto(request):
    return render(request, "app/buscarTinto.html")

def buscar2(request):
    if request.GET['precio']:
        precio = request.GET['precio']
        cursos = Tinto.objects.filter(precio__icontains=precio)
        return render(request,
                      "app/resultadosTinto.html",
                     {"precio":precio, "db":cursos})
    
    return HttpResponse("No se ingresaron datos para la búsqueda")

def buscarBlanco(request):
    return render(request, "app/blanco.html")

def buscar3(request):
    if request.GET['precio']:
        precio = request.GET['precio']
        cursos = Blancos.objects.filter(precio__icontains=precio)
        return render(request,
                      "app/resultadosBlancos.html",
                     {"precio":precio, "db":cursos})
    
    return HttpResponse("No se ingresaron datos para la búsqueda")


def buscarCliente(request):
    return render(request, "app/cliente.html")

def buscar(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        cursos = Cliente.objects.filter(nombre__icontains=nombre)
        return render(request,
                      "app/resultadosClientes.html",
                     {"precio":nombre, "db":cursos})
    
    return HttpResponse("No se ingresaron datos para la búsqueda")

def formBlanco(request):
    if request.method == "POST":
        curso2 = Blancos(nombre=request.POST['nombre'], precio=request.POST['precio'])
        curso2.save()
        return HttpResponse("Se grabó con exito")
    

    return render(request, "app/blancoForm.html")

def formBlanco2(request):
     if request.method == "POST":
        miForm2 = formBlanco(request.POST)
        if miForm2.is_valid: 
             informacion = miForm2.cleaned_data
             curso2 = Blancos(nombre=informacion['nombre'], precio=informacion['precio'])
             curso2.save()
             return render(request, "app/base.html")

     else:
         miForm2 = formBlanco()
        
        
         return render(request, "app/rubiaForm2.html", {"form":miForm2})


def formCliente(request):
    if request.method == "POST":
        curso = Cliente(nombre=request.POST['nombre'], apellido=request.POST['apellido'], email=request.POST['email'], telefono=request.POST['telefono'])
        curso.save()
        return HttpResponse("Se grabó con exito")
    

    return render(request, "app/clienteForm.html")

def formCliente2(request):
     if request.method == "POST":
        miForm = formCliente(request.POST)
        if miForm.is_valid: 
             informacion = miForm.cleaned_data
             curso = Cliente(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], telefono=informacion['telefono'])
             curso.save()
             return render(request, "app/base.html")

     else:
         miForm = formCliente()
        
        
         return render(request, "app/clienteForm2.html", {"form":miForm})
