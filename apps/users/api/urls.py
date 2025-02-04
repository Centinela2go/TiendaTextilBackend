from django.urls import path

from apps.users.api.api import UserAPIView

urlpatterns = [
    path('usuario/', UserAPIView.as_view(), name='usuario_api'),
    path('usuario/<int:pk>/', UserAPIView.as_view(), name='usuario_api_detail')
]
