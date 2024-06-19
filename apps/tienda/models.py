from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.users.models import Base, User

import re
#comentario
# validar numero telefonico
def validate_phone_number(value):
    if not value.isdigit():
        raise ValidationError('El número de teléfono debe contener solo dígitos.')
    if len(value) != 9:
        raise ValidationError('El número de teléfono debe tener exactamente 9 dígitos.')
    
# Validador de dirección
def validate_home_address(value):
    """
    Valida que la dirección de casa contenga solo letras, números, espacios
    y los caracteres ,.-.
    """
    if not re.match(r'^[a-zA-Z0-9\s,.-]+$', value):
        raise ValidationError(
            'La dirección solo puede contener letras, números, espacios '
            'y los caracteres ,.-'
        )

# Create your models here.

class Categoria(Base):
    nombre = models.CharField('Nombre :', max_length=80)
    descripcion = models.CharField('Descripcion :', max_length= 200)

class Proveedor(Base):
    nombre = models.CharField('Nombre :', max_length=80)
    direccion =models.CharField('Direccion :', max_length= 80,validators=[validate_home_address])
    telefono =models.CharField('Telefono :', max_length= 9,validators=[validate_phone_number])
    email =models.EmailField('Email :', max_length= 20)
    
class Cliente(Base):
    nombre = models.CharField('Nombre :', max_length=80)
    direccion =models.CharField('Direccion :', max_length= 80,validators=[validate_home_address])
    telefono =models.CharField('Telefono :', max_length= 9,validators=[validate_phone_number])
    email =models.EmailField('Email :', max_length= 20)
    


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