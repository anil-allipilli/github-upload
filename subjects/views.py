from django.shortcuts import render

from .serializers import GradeSerializer, SubjectSerializer, SectionSerializer
from rest_framework import permissions
from rest_framework import viewsets
from .models import Grade, Subject, Section



class GradeViewSet(viewsets.ModelViewSet):  

    queryset = Grade.objects.all()
    serializer_class = GradeSerializer   
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class SubjectViewSet(viewsets.ModelViewSet):  

    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer   
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)



class SectionViewSet(viewsets.ModelViewSet):  

    queryset = Section.objects.all()
    serializer_class = SectionSerializer   
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

