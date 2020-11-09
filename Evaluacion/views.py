from django.shortcuts import render
from django.http import HttpResponse
from .forms import ImageForm

def index(request):
    return render(request, 'index.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def productos(request):
    return render(request, 'productos.html')

def registro(request):
    return render(request, 'registro.html')   

def login(request):
    return render(request, 'login.html') 

def logout(request):
    return render(request, 'login.html') 

def homeTest(request):
    pagina = """<a href="https://hometest.cl/"> """
    return HttpResponse (pagina)

def galeria(request):
    return render(request,'galeria.html')

def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'galeria.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'galeria.html', {'form': form})
