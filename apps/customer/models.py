from django.db import models

from apps.helpers.models import TimeStamp
from apps.house.models import Apartment
from apps.user.models import Customer


# Create your models here.
class Booking(TimeStamp):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name='apartment_booking')
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True, related_name='user_booking')
    is_confirm = models.BooleanField(default=False)
    is_cancel = models.BooleanField(default=False)
