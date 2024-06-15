from rest_framework import serializers

from apps.tienda.models import Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        exclude = ('fecha_registro', 'fecha_actualizacion', 'creado_por', 'actualizado_por')