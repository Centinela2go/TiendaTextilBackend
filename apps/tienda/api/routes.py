from rest_framework.routers import DefaultRouter
from apps.tienda.api.views.general import CategoriaViewSet

router = DefaultRouter()

router.register('producto/categoria', CategoriaViewSet, basename='producto_categoria') 


urlpatterns = router.urls