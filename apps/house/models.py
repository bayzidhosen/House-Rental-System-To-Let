from django.db import models
from django.db.models import SET_NULL

from apps.helpers.models import TimeStamp
from apps.location.models import Division, District, UpazilaOrThana, UnionOrWard
from apps.user.models import HouseOwner


# Create your models here.
class Apartment(TimeStamp):
    title = models.CharField(max_length=255)
    owner = models.ForeignKey(HouseOwner, on_delete=models.CASCADE, null=True, blank=True, related_name='owner_house')
    description = models.TextField(blank=True)
    room = models.FloatField(default=0)
    area = models.PositiveIntegerField(default=0)
    floor = models.PositiveIntegerField(default=0, verbose_name='Total Floor')
    parking = models.BooleanField(default=True)
    lift = models.BooleanField(default=True)
    stair = models.BooleanField(default=True)
    thumbnail = models.ImageField(upload_to='thumbnail', null=True, blank=True)
    image_1 = models.ImageField(upload_to='thumbnail', null=True, blank=True)
    image_2 = models.ImageField(upload_to='thumbnail', null=True, blank=True)
    image_3 = models.ImageField(upload_to='thumbnail', null=True, blank=True)

    # present address
    division = models.ForeignKey(Division, on_delete=SET_NULL, null=True, blank=True)
    district = models.ForeignKey(District, on_delete=SET_NULL, null=True, blank=True)
    thana = models.ForeignKey(UpazilaOrThana, on_delete=SET_NULL, null=True, blank=True)
    union = models.ForeignKey(UnionOrWard, on_delete=SET_NULL, null=True, blank=True)

    address = models.CharField(max_length=255)
    rent = models.PositiveIntegerField(default=0)
    is_rent_complete = models.BooleanField(default=False)

    def no_of_app(self):
        t = self.apartment_booking.count()
        return t if t else 0

    def __str__(self):
        return self.title


# Create your models here.
class Contact(TimeStamp):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name
