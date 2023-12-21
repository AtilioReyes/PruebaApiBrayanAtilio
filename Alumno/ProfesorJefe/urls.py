from django.urls import path, include
from . import api
from rest_framework import routers
from .api import profeViewSet



router = routers.DefaultRouter()
router.register('curso', api.profeViewSet)


urlpatterns = [
    path('', include(router.urls))
]
