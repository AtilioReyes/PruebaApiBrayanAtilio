from django.urls import path, include
from . import api
from rest_framework import routers
from .api import cursoViewSet, alumnoViewSet



router = routers.DefaultRouter()
router.register('curso', api.cursoViewSet)
router.register('alumno', api.alumnoViewSet)

urlpatterns = [
    path('', include(router.urls))
]

