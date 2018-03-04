from rest_framework import serializers

from parkfinder.parks.models import Park, ParkAmenity, AmenityType


class AmenityTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AmenityType
        fields = '__all__'


class ParkAmenitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ParkAmenity
        fields = '__all__'


class ParkAmenityNestedSerializer(serializers.ModelSerializer):
    amenity = serializers.SlugRelatedField(
        source='amenity_type', read_only=True, slug_field='description')

    class Meta:
        model = ParkAmenity
        fields = (
            'amenity', 'count', 'size', 'size_unit', 'notes',
        )


class ParkSerializer(serializers.HyperlinkedModelSerializer):
    park_amenities = ParkAmenityNestedSerializer(many=True)

    class Meta:
        model = Park
        exclude = ('amenities',)


