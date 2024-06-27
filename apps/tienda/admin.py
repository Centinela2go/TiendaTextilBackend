from django.contrib import admin

from apps.tienda.models import Categoria, Proveedor, ProductoAlmacen, Producto, Empleado

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Proveedor)
admin.site.register(ProductoAlmacen)
admin.site.register(Producto)
admin.site.register(Empleado)