from rest_framework import viewsets
from parkfinder.parks.models import Park, AmenityType, ParkAmenity

from . import serializers


class ParkViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Park.objects.all()
    serializer_class = serializers.ParkSerializer


class AmenityTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AmenityType.objects.all()
    serializer_class = serializers.AmenityTypeSerializer


class ParkAmenityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ParkAmenity.objects.select_related().all()
    serializer_class = serializers.ParkAmenitySerializer
