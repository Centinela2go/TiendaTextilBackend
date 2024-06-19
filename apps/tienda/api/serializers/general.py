from rest_framework import serializers

from apps.tienda.models import Categoria, Cliente, ProductoAlmacen, Proveedor

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
    class Meta:
        model = ProductoAlmacen
        exclude = ('fecha_registro', 'fecha_actualizacion', 'creado_por', 'actualizado_por')