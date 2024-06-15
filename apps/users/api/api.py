from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from apps.users.api.serializers import UserSerializer
from apps.users.models import User

class UserAPIView(APIView):
    def get(self, request, pk = None):
        if (pk):
            user = get_object_or_404(User, id=pk)
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        users = User.objects.all()
        user_serializer = UserSerializer(users, many = True)
        return Response(user_serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        user_serializer = UserSerializer(data=request.data)
        
        if (user_serializer.is_valid()):
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        user_serializer = UserSerializer(user, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)