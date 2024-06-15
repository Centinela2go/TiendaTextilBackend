from django.urls import path

from apps.tienda.api.views.general import CategoriaListAPIView

urlpatterns = [
    path('categoria/', CategoriaListAPIView.as_view(), name = 'categoria_list'),
]
