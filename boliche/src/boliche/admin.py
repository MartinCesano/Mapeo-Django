from django.contrib import admin
from .models import Barra, Venta, DetalleVenta, Consumicion, DetalleConsumicion, Ingrediente

class DetalleVentaInline(admin.TabularInline):
    model = DetalleVenta
    extra = 1

class VentaAdmin(admin.ModelAdmin):
    inlines = [DetalleVentaInline]

class DetalleConsumicionInline(admin.TabularInline):
    model = DetalleConsumicion
    extra = 1

class ConsumicionAdmin(admin.ModelAdmin):
    inlines = [DetalleConsumicionInline]

admin.site.register(Barra)
admin.site.register(Venta, VentaAdmin)
admin.site.register(DetalleVenta)
admin.site.register(Consumicion, ConsumicionAdmin)
admin.site.register(DetalleConsumicion)
admin.site.register(Ingrediente)
