from django.db import transaction
from django.db.models import ProtectedError
from django.db.utils import IntegrityError
from rest_framework import generics, status
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import DjangoModelPermissions

from apps.tienda.models import *
from apps.tienda.api.serializers.general import *
from apps.users.permissions import IsInDynamicGroup

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
    
    
class CategoriaViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriaSerializer
    permission_classes = [IsInDynamicGroup]
    allowed_groups = ['administrador', 'empleado']

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter()

    def get_object(self):
        return self.get_serializer().Meta.model.objects.filter(id=self.kwargs['pk'])

    @swagger_auto_schema(
        operation_description="Get a list of items",
        responses={200: openapi.Response('Success', CategoriaSerializer)},
        security=[{'Bearer': []}]
    )
    def list(self, request):
        data = self.get_queryset()
        data = self.get_serializer(data, many=True)
        data = {
            "total": self.get_queryset().count(),
            "totalNotFiltered": self.get_queryset().count(),
            "rows": data.data
        }
        return Response(data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Categoria del producto registrado correctamente!'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        if self.get_object().exists():
            data = self.get_object().get()
            data = self.get_serializer(data)
            return Response(data.data)
        return Response({'message':'', 'error':'Categoria del producto no encontrado!'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_object().exists():
            serializer = self.serializer_class(instance=self.get_object().get(), data=request.data)       
            if serializer.is_valid():       
                serializer.save()       
                return Response({'message':'Categoria del producto actualizado correctamente!'}, status=status.HTTP_200_OK)       
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)    

    def destroy(self, request, pk=None):       
        if self.get_object().exists():
            try:
                self.get_object().get().delete()       
                return Response({'message':'Categoria del producto eliminado correctamente!'}, status=status.HTTP_200_OK)       
            except ProtectedError:
                return Response({'message':'No se puede eliminar la categoría del producto porque está siendo referenciada por otro registro.', 'error':{'ReferenciaError': ['Error No se puede eliminar la categoría del producto porque está siendo referenciada por otro registro.']}}, status=status.HTTP_400_BAD_REQUEST)
            except IntegrityError:
                return Response({'message':'Error de integridad al eliminar la categoría del producto.', 'error':['Error de integridad al eliminar la categoría del producto.']}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'', 'error':['Categoria del producto no encontrado!']}, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, *args, **kwargs):
        if self.get_object().exists():
            serializer = self.serializer_class(instance=self.get_object().get(), data=request.data, partial=True)       
            if serializer.is_valid():       
                serializer.save()       
                return Response({'message':'Categoria del producto actualizado correctamente!'}, status=status.HTTP_200_OK)       
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST) 
       
class ProveedorViewSet(viewsets.ModelViewSet):
    serializer_class = ProveedorSerializer
    permission_classes = [IsInDynamicGroup]
    allowed_groups = ['administrador', 'empleado']

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter()

    def get_object(self):
        return self.get_serializer().Meta.model.objects.filter(id=self.kwargs['pk'])

    def list(self, request):
        data = self.get_queryset()
        data = self.get_serializer(data, many=True)
        data = {
            "total": self.get_queryset().count(),
            "totalNotFiltered": self.get_queryset().count(),
            "rows": data.data
        }
        return Response(data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Proveedor registrado correctamente!'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        if self.get_object().exists():
            data = self.get_object().get()
            data = self.get_serializer(data)
            return Response(data.data)
        return Response({'message':'', 'error':'Proveedor no encontrado!'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_object().exists():
            serializer = self.serializer_class(instance=self.get_object().get(), data=request.data)       
            if serializer.is_valid():       
                serializer.save()       
                return Response({'message':'Proveedor actualizado correctamente!'}, status=status.HTTP_200_OK)       
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)    

    def destroy(self, request, pk=None):       
        if self.get_object().exists():       
            self.get_object().get().delete()       
            return Response({'message':'Proveedor eliminado correctamente!'}, status=status.HTTP_200_OK)       
        return Response({'message':'', 'error':'Proveedor no encontrado!'}, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, *args, **kwargs):
        if self.get_object().exists():
            serializer = self.serializer_class(instance=self.get_object().get(), data=request.data, partial=True)       
            if serializer.is_valid():       
                serializer.save()       
                return Response({'message':'Proveedor actualizado correctamente!'}, status=status.HTTP_200_OK)       
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST) 
    
    
class ClienteViewSet(viewsets.ModelViewSet):
    serializer_class = ClienteSerializer
    permission_classes = [IsInDynamicGroup]
    allowed_groups = ['administrador', 'empleado']

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter()

    def get_object(self):
        return self.get_serializer().Meta.model.objects.filter(id=self.kwargs['pk'])

    def list(self, request):
        data = self.get_queryset()
        data = self.get_serializer(data, many=True)
        data = {
            "total": self.get_queryset().count(),
            "totalNotFiltered": self.get_queryset().count(),
            "rows": data.data
        }
        return Response(data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Cliente registrado correctamente!'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        if self.get_object().exists():
            data = self.get_object().get()
            data = self.get_serializer(data)
            return Response(data.data)
        return Response({'message':'', 'error':'Cliente no encontrado!'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        
        if self.get_object().exists():
            serializer = self.serializer_class(instance=self.get_object().get(), data=request.data)       
            if serializer.is_valid():       
                serializer.save()       
                return Response({'message':'Cliente actualizado correctamente!'}, status=status.HTTP_200_OK)       
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)    

    def destroy(self, request, pk=None):       
        if self.get_object().exists():       
            self.get_object().get().delete()       
            return Response({'message':'Cliente eliminado correctamente!'}, status=status.HTTP_200_OK)       
        return Response({'message':'', 'error':'Cliente no encontrado!'}, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, *args, **kwargs):
        if self.get_object().exists():
            serializer = self.serializer_class(instance=self.get_object().get(), data=request.data, partial=True)       
            if serializer.is_valid():       
                serializer.save()       
                return Response({'message':'Cliente actualizado correctamente!'}, status=status.HTTP_200_OK)       
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST) 
    
class ProductoAlmacenViewSet(viewsets.ModelViewSet):
    serializer_class = ProductoAlmacenSerializer
    serializer_class_post = ProductoAlmacenPostSerializer
    permission_classes = [IsInDynamicGroup]
    allowed_groups = ['administrador', 'empleado']

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter()

    def get_object(self):
        return self.get_serializer().Meta.model.objects.filter(id=self.kwargs['pk'])

    def list(self, request):
        data = self.get_queryset()
        data = self.get_serializer(data, many=True)
        data = {
            "total": self.get_queryset().count(),
            "totalNotFiltered": self.get_queryset().count(),
            "rows": data.data
        }
        return Response(data)

    def create(self, request):
        serializer = self.serializer_class_post(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Producto registrado correctamente!'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        if self.get_object().exists():
            data = self.get_object().get()
            data = self.get_serializer(data)
            return Response(data.data)
        return Response({'message':'', 'error':'Producto no encontrado!'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_object().exists():
            serializer = self.serializer_class_post(instance=self.get_object().get(), data=request.data)       
            if serializer.is_valid():       
                serializer.save()       
                return Response({'message':'Producto actualizado correctamente!'}, status=status.HTTP_200_OK)       
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)    

    def destroy(self, request, pk=None):       
        if self.get_object().exists():       
            self.get_object().get().delete()       
            return Response({'message':'Producto eliminado correctamente!'}, status=status.HTTP_200_OK)       
        return Response({'message':'', 'error':'Producto no encontrado!'}, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, *args, **kwargs):
        if self.get_object().exists():
            serializer = self.serializer_class(instance=self.get_object().get(), data=request.data, partial=True)       
            if serializer.is_valid():       
                serializer.save()       
                return Response({'message':'Producto actualizado correctamente!'}, status=status.HTTP_200_OK)       
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST) 
    
    
class ProductoViewSet(viewsets.ModelViewSet):
    serializer_class = ProductoSerializer
    serializer_class_post = ProductoPostSerializer
    permission_classes = [IsInDynamicGroup]
    allowed_groups = ['administrador', 'empleado'] 

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter()

    def get_object(self):
        return self.get_serializer().Meta.model.objects.filter(id=self.kwargs['pk'])
    
    def list(self, request):
        data = self.get_queryset()
        data = self.get_serializer(data, many=True)
        data = {
            "total": self.get_queryset().count(),
            "totalNotFiltered": self.get_queryset().count(),
            "rows": data.data
        }
        return Response(data)

    def create(self, request):
        serializer = self.serializer_class_post(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Producto registrado correctamente!'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        if self.get_object().exists():
            data = self.get_object().get()
            data = self.get_serializer(data)
            return Response(data.data)
        return Response({'message':'', 'error':'Producto no encontrado!'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_object().exists():
            serializer = self.serializer_class_post(instance=self.get_object().get(), data=request.data)       
            if serializer.is_valid():       
                serializer.save()       
                return Response({'message':'Producto actualizado correctamente!'}, status=status.HTTP_200_OK)       
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)    

    def destroy(self, request, pk=None):       
        if self.get_object().exists():       
            self.get_object().get().delete()       
            return Response({'message':'Producto eliminado correctamente!'}, status=status.HTTP_200_OK)       
        return Response({'message':'', 'error':'Producto no encontrado!'}, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, *args, **kwargs):
        if self.get_object().exists():
            serializer = self.serializer_class(instance=self.get_object().get(), data=request.data, partial=True)       
            if serializer.is_valid():       
                serializer.save()       
                return Response({'message':'Producto actualizado correctamente!'}, status=status.HTTP_200_OK)       
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST) 
    
    
class EmpleadoViewSet(viewsets.ModelViewSet):
    serializer_class = EmpleadoSerializer
    permission_classes = [IsInDynamicGroup]
    allowed_groups = ['administrador']
    

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(estado = True)

    def get_object(self):
        return self.get_serializer().Meta.model.objects.filter(id=self.kwargs['pk'], estado = True)

    def list(self, request):
        data = self.get_queryset()
        data = self.get_serializer(data, many=True)
        data = {
            "total": self.get_queryset().count(),
            "totalNotFiltered": self.get_queryset().count(),
            "rows": data.data
        }
        return Response(data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Empleado registrado correctamente!'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        if self.get_object().exists():
            data = self.get_object().get()
            data = self.get_serializer(data)
            return Response(data.data)
        return Response({'message':'', 'error':'Empleado no encontrado!'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_object().exists():
            serializer = self.serializer_class(instance=self.get_object().get(), data=request.data)       
            if serializer.is_valid():       
                serializer.save()       
                return Response({'message':'Empleado actualizado correctamente!'}, status=status.HTTP_200_OK)       
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)    

    def destroy(self, request, pk=None):       
        if self.get_object().exists():       
            self.get_object().get().delete()       
            return Response({'message':'Empleado eliminado correctamente!'}, status=status.HTTP_200_OK)       
        return Response({'message':'', 'error':'Empleado no encontrado!'}, status=status.HTTP_400_BAD_REQUEST)
    
class VentaViewSet(viewsets.ViewSet):
    permission_classes = [IsInDynamicGroup]
    allowed_groups = ['administrador', 'empleado']
    permissions_extra = ['add_orden']
    
    def create(self, request):
        with transaction.atomic():
            # crear una orden (venta)
            venta = {"empleado": request.user.id, "total": 0}
            serializer_venta = OrdenSerializer(data=venta)
            if not serializer_venta.is_valid():
                raise Exception("Error: No se pudo realizar la venta")
            venta_instance = serializer_venta.save()
            
            productos = request.data.get("productos", [])
            
            if (len(productos) <= 0):
                raise Exception("Numero de productos invalidos")
            total = 0
            for producto in productos:    
                prod_bd = ProductoAlmacen.objects.filter(producto__id=producto["id"]).first()
                
                if (not prod_bd):
                    raise("Producto no existe")
                
                stock = prod_bd.existencias
                if (stock - producto["cantidad"] < 0):
                    raise Exception("Stock insuficiente ingrese otra cantidad")
                prod_bd.existencias -= producto["cantidad"]
                prod_bd.save()
                
                prod = Producto.objects.filter(pk=producto["id"]).first()
                total += prod.precio * producto["cantidad"]
                detalle = {"orden": venta_instance.pk, "producto": producto["id"], "cantidad": producto["cantidad"], "precio_unitario": prod.precio }
                serializer_detalle = DetalleOrdenSerializer(data=detalle)
                if (not serializer_detalle.is_valid()):
                    raise Exception("Error al realizar venta")
                serializer_detalle.save()
            venta_instance.total = total
            venta_instance.save()
            print(request.data)
        return Response({'message': 'Empleado registrado correctamente'}, status=status.HTTP_201_CREATED)
        