from rest_framework.routers import DefaultRouter
from django.urls import include, path

from core.views import (
  	CarViewset,
)


router = DefaultRouter()
router.register(
    r'car',
    CarViewset,
    basename='car'
)

urlpatterns = [
    path('api/', include(router.urls)),
]
