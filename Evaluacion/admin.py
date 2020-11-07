from django.contrib import admin

from Evaluacion.models import Zapato

class ZapatoAdmin(admin.ModelAdmin):
    search_fields=("marca", "color","talla", "material")
    list_filter=("marca", "color","talla", "material",)

admin.site.register(Zapato, ZapatoAdmin)