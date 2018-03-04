from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'parks', views.ParkViewSet)
router.register(r'amenitytypes', views.AmenityTypeViewSet)
router.register(r'parkamenities', views.ParkAmenityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
