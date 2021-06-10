from django.contrib import admin
from Modulos.ordenes.models import *
# Register your models here.

admin.site.register(orden)
class ordenAdmin(admin.ModelAdmin):
    ordering=('fecha')
    list_display=('ot', 'matricula', 'cliente', 'estado', 'fecha')
    search_fields=('ot','matricula', 'cliente', 'estado')
    list_per_page=20
    
admin.site.register(contabilidad)
class contabilidadAdmin(admin.ModelAdmin):
    ordering=('fecha')
    list_display=('orden_trabajo', 'pago', 'precio')
    search_fields=('orden_trabajo','pago')
    list_display_links=('orden_trabajo')
    list_per_page=20
