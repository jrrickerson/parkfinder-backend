from django.db import models


class AmenityType(models.Model):
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.description


class Park(models.Model):
    # Descriptive
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    zipcode = models.CharField(max_length=50)
    county = models.CharField(max_length=250)
    district = models.IntegerField(null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    notes = models.TextField(blank=True)

    former_name = models.CharField(max_length=250, blank=True)
    neighborhood = models.CharField(max_length=250, blank=True)

    # Administrative Fields
    global_id = models.UUIDField()
    park_id = models.CharField(max_length=50)
    parcel_id = models.CharField(max_length=250)
    shape_length = models.FloatField(null=True)
    shape_area = models.FloatField(null=True)
    park_class = models.CharField(
        max_length=50, blank=True, verbose_name='class')
    npu1 = models.CharField(max_length=250, blank=True)

    amenities = models.ManyToManyField(
        AmenityType, through='ParkAmenity', related_name='parks')

    def __str__(self):
        return self.name


class ParkAmenity(models.Model):
    park = models.ForeignKey(
        Park, on_delete=models.CASCADE, related_name='park_amenities')
    amenity_type = models.ForeignKey(AmenityType, on_delete=models.CASCADE)

    count = models.IntegerField()
    size = models.IntegerField(default=0)
    size_unit = models.CharField(max_length=50, blank=True)
    notes = models.TextField(blank=True)
