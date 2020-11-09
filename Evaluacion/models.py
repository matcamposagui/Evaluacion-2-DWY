from django.db import models

class Zapato (models.Model):
    marca=models.TextField(max_length=50)
    material=models.TextField(max_length=50)
    color=models.TextField(max_length=50)
    talla=models.TextField(max_length=50)
    image = models.ImageField(verbose_name="Imagen", upload_to="Galeria", null="false")

    def __str__(self):
        return 'Zapato marca %s'%(self.marca)


class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title