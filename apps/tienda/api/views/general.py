from rest_framework import generics

from apps.tienda.models import Categoria
from apps.tienda.api.serialiers.general import CategoriaSerializer

class GeneralListAPIView(generics.ListAPIView):
    serializer_class = None
    
    def get_queryset(self):
        instance = self.get_serializer().Meta.model
        return instance.objects.filter(estado = True)

class CategoriaListAPIView(GeneralListAPIView):
    serializer_class = CategoriaSerializer
