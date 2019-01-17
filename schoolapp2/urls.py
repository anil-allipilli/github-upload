from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from profiles import views as profileviews
from subjects import views as subjectviews

router = DefaultRouter()

router.register('grades', subjectviews.GradeViewSet, 'grade')
router.register('subjects', subjectviews.SubjectViewSet, 'subject')
router.register('sections', subjectviews.SectionViewSet, 'section')

router.register(r'teachers', profileviews.TeacherViewSet)
router.register(r'students', profileviews.StudentViewSet)
router.register(r'parents', profileviews.GaurdianViewSet)
router.register(r'studentperformanceprofile', profileviews.StudentPerformanceProfileViewSet)
router.register(r'studentmedicalprofile', profileviews.StudentMedicalInformationProfileViewSet)
router.register(r'studenttaskprofile', profileviews.StudentTaskProfileViewSet)
router.register(r'medicalassistance', profileviews.MedicalAssistanceViewSet)
router.register(r'teachertaskprofile', profileviews.TeacherTaskProfileViewSet)
router.register(r'parenttaskprofile', profileviews.ParentTaskProfileViewSet)
router.register(r'driverprofile', profileviews.DriverViewSet)
router.register(r'bus', profileviews.BusViewSet)
router.register(r'nurses', profileviews.PhysicianViewSet)
router.register(r'workingstaff', profileviews.WorkingStaffViewSet)
router.register(r'management', profileviews.ManagementStaffViewSet)



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls, namespace="api")),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
