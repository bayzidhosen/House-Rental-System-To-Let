# Create your views here.
from django.views.generic import ListView

from apps.customer.models import Booking


class MyApplyView(ListView):
    model = Booking
    template_name = 'my_apply.html'

    def get_queryset(self):
        qs = super(MyApplyView, self).get_queryset()
        qs = qs.filter(user=self.request.user.pk)
        return qs
