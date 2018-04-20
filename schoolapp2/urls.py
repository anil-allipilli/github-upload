from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from profiles import views as profileviews
from subjects import views as subjectviews

router = DefaultRouter()

router.register('grades', subjectviews.GradeViewSet, 'grade')
router.register('subjects', subjectviews.SubjectViewSet, 'subject')
router.register('sections', subjectviews.SectionViewSet, 'section')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls, namespace="api")),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
