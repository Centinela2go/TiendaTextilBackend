from rest_framework import serializers

from apps.tienda.models import Categoria, Cliente, ProductoAlmacen, Proveedor, Producto, Empleado
from apps.users.api.serializers import CustomUserSerializer

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        exclude = ('fecha_registro', 'fecha_actualizacion', 'creado_por', 'actualizado_por')
        
class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        exclude = ('fecha_registro', 'fecha_actualizacion', 'creado_por', 'actualizado_por')
        
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        exclude = ('fecha_registro', 'fecha_actualizacion', 'creado_por', 'actualizado_por')
        
class ProductoAlmacenSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer()
    proveedor = ProveedorSerializer()
    class Meta:
        model = ProductoAlmacen
        exclude = ('fecha_registro', 'fecha_actualizacion', 'creado_por', 'actualizado_por')
        
class ProductoAlmacenPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoAlmacen
        exclude = ('fecha_registro', 'fecha_actualizacion', 'creado_por', 'actualizado_por')
     
        
class ProductoSerializer(serializers.ModelSerializer):
    producto_almacen = ProductoAlmacenSerializer()
    class Meta:
        model = Producto
        exclude = ('fecha_registro', 'fecha_actualizacion', 'creado_por', 'actualizado_por')
        
class ProductoPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        exclude = ('fecha_registro', 'fecha_actualizacion', 'creado_por', 'actualizado_por')
        
class EmpleadoSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    class Meta:
        model = Empleado
        exclude = ('fecha_registro', 'fecha_actualizacion', 'creado_por', 'actualizado_por')