from django.urls import path, include
from rest_framework import routers

from apps.customer.booking import BookingViewSet

router = routers.DefaultRouter()
router.register(r'bookings', BookingViewSet, basename='booking')

urlpatterns = [
    path('', include(router.urls)),
]
