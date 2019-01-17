from django.shortcuts import render
from .models import MyUser
from .serializers import MyUserSerializer
from rest_framework import permissions
from rest_framework import viewsets


class MyAbstractUserViewSet(viewsets.ModelViewSet):  

    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer   
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)