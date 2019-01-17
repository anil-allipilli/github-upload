from django.shortcuts import render
from .models import *
from .serializers import *
# from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.decorators import api_view, action
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, mixins, generics, renderers, viewsets
# from .permissions import IsOwnerOrReadOnly
from rest_framework.reverse import reverse

from rest_framework.authentication import TokenAuthentication






class TeacherViewSet(viewsets.ModelViewSet):

    queryset = SchoolTeacher.objects.all()
    serializer_class = TeacherSerializer
    # authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                            #IsOwnerOrReadOnly,
                            )
    # @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    # def note_title(self, request, *args, **kwargs):
    #     notes = self.get_object()
    #     return Response(notes.title)
    
    # def perform_create(self, serializer):
    #     serializer.save(notes_author=SchoolTeacher.objects.get(teacher=self.request.user))


class StudentViewSet(viewsets.ModelViewSet):

    queryset = Scholar.objects.all()
    serializer_class = StudentSerializer
    # authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                            #IsOwnerOrReadOnly,
                            )

class GaurdianViewSet(viewsets.ModelViewSet):

    queryset = Gaurdian.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                            #IsOwnerOrReadOnly,
                            )

class StudentPerformanceProfileViewSet(viewsets.ModelViewSet):

    queryset = StudentPerformanceProfile.objects.all()
    serializer_class = StudentPerformanceProfileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                            #IsOwnerOrReadOnly,
                            )

class StudentMedicalInformationProfileViewSet(viewsets.ModelViewSet):

    queryset = StudentMedicalInformationProfile.objects.all()
    serializer_class = StudentMedicalInformationProfileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                            #IsOwnerOrReadOnly,
                            )

class StudentTaskProfileViewSet(viewsets.ModelViewSet):

    queryset = StudentTaskProfile.objects.all()
    serializer_class = StudentTaskProfileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                            #IsOwnerOrReadOnly,
                            )
class MedicalAssistanceViewSet(viewsets.ModelViewSet):

    queryset = MedicalAssistance.objects.all()
    serializer_class = MedicalAssistanceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                            #IsOwnerOrReadOnly,
                            )

class TeacherTaskProfileViewSet(viewsets.ModelViewSet):

    queryset = TeacherTaskProfile.objects.all()
    serializer_class = TeacherTaskProfileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                            #IsOwnerOrReadOnly,
                            )

class ParentTaskProfileViewSet(viewsets.ModelViewSet):

    queryset = ParentTaskProfile.objects.all()
    serializer_class = ParentTaskProfileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                            #IsOwnerOrReadOnly,
                            )

class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                            #IsOwnerOrReadOnly,
                            )

class BusViewSet(viewsets.ModelViewSet):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                            #IsOwnerOrReadOnly,
                            )

class PhysicianViewSet(viewsets.ModelViewSet):
    queryset = Physician.objects.all()
    serializer_class = PhysicianSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                            #IsOwnerOrReadOnly,
                            )

class WorkingStaffViewSet(viewsets.ModelViewSet):
    queryset = WorkingStaff.objects.all()
    serializer_class = WorkingStaffSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                            #IsOwnerOrReadOnly,
                            )

class ManagementStaffViewSet(viewsets.ModelViewSet):
    queryset = ManagementStaff.objects.all()
    serializer_class = ManagementStaffSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                            #IsOwnerOrReadOnly,
                            )