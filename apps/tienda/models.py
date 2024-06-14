from django.db import models
from apps.users.models import Base, User
from django.utils.translation import gettext_lazy as _
#comentario
# Create your models here.

class Categoria:
    pass
class Proveedor:
    pass
class Cliente:
    pass

class ProductoAlmacen(Base):
    nombre = models.CharField(max_length=255)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    existencias = models.IntegerField(default=0)  
    descripcion = models.CharField(max_length=255, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre
    
class Producto(Base):
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    producto_almacen = models.OneToOneField(ProductoAlmacen, on_delete=models.PROTECT)

    def __str__(self):
        return self.producto_almacen.nombre
    
class Empleado(models.Model):
    nombre = models.CharField(max_length=255)
    puesto = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)
    fecha_contratacion = models.DateField()
    seguro_medico = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre
    
class Orden(models.Model):
    class EstadoOrden(models.TextChoices):
        PEDIDO = 'PEDIDO', _('Pedido')
        ENTREGADO = 'ENTREGADO', _('Entregado')
        CANCELADO = 'CANCELADO', _('Cancelado')

    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, blank=True, null=True)
    fecha = models.DateTimeField()
    empleado = models.ForeignKey(Empleado, on_delete=models.PROTECT)
    estado_orden = models.CharField(
        max_length=20,
        choices=EstadoOrden.choices,
        default=EstadoOrden.PEDIDO
    )
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Orden {self.id} - {self.cliente.nombre}'
    
class DetalleOrden(models.Model):
    orden = models.ForeignKey(Orden, on_delete=models.PROTECT)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Detalle Orden {self.id} - Producto {self.producto_id} - Cantidad {self.cantidad}"