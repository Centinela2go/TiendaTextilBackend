from rest_framework.routers import DefaultRouter
from apps.tienda.api.views.general import (CategoriaViewSet, ProductoAlmacenViewSet, 
                                           ProveedorViewSet, ProductoViewSet, 
                                           ClienteViewSet, EmpleadoViewSet)

router = DefaultRouter()

router.register('producto/categoria', CategoriaViewSet, basename='producto_categoria') 
router.register('proveedor', ProveedorViewSet, basename='proveedor') 
router.register('cliente', ClienteViewSet, basename='cliente') 
router.register('almacen/producto', ProductoAlmacenViewSet, basename='producto_almacen') 
router.register('producto', ProductoViewSet, basename='producto') 
router.register('empleado', EmpleadoViewSet, basename='empleado') 


urlpatterns = router.urls