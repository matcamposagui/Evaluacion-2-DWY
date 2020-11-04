from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def productos(request):
    return render(request, 'productos.html')

def registro(request):
    return render(request, 'registro.html')   

def homeTest(request):
    pagina = """<a href="https://hometest.cl/"> """
    return HttpResponse (pagina)



