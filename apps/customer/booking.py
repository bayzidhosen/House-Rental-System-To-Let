from rest_framework import serializers, status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.customer.models import Booking
from apps.helpers.utils import CsrfExemptSessionAuthentication


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class BookingViewSet(viewsets.ModelViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
