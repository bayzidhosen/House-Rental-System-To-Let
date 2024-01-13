# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView, CreateView, DetailView

from apps.customer.models import Booking
from apps.helpers.views import PageHeaderMixin
from apps.house.models import Apartment
from apps.owner.forms import MyApartmentForm


class MyApartmentListView(ListView):
    model = Apartment
    paginate_by = 20
    ordering = '-created_at'
    template_name = 'my_apartments.html'

    def get_queryset(self):
        qs = self.model.objects.filter(owner=self.request.user)
        return qs


class MyApartmentView(ListView):
    model = Booking
    template_name = 'apartments_apply.html'

    def get_queryset(self):
        qs = super(MyApartmentView, self).get_queryset()
        pk = self.kwargs['pk']
        qs = qs.filter(apartment=pk)
        return qs


class MyApartmentCreateView(CreateView):
    model = Apartment
    form_class = MyApartmentForm
    template_name = 'add.html'
    success_url = reverse_lazy('my_apartments')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class MyApartmentUpdateView(UpdateView):
    model = Apartment
    form_class = MyApartmentForm
    template_name = 'add.html'
    success_url = reverse_lazy('my_apartments')


class MyApartmentDeleteView(PageHeaderMixin, DeleteView):
    model = Apartment
    template_name = 'delete.html'
    page_title = 'Buyer'
    success_url = reverse_lazy('my_apartments')
