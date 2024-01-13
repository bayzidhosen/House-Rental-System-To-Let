from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView
from django_filters.views import FilterView

from apps.customer.models import Booking
from apps.helpers.views import PageHeaderMixin
from apps.house.filters import ApartmentFilters
from apps.house.forms import ApartmentForm, ContactForm
from apps.house.models import Apartment, Contact


# Create your views here.
class DashboardView(TemplateView):
    template_name = 'home.html'


class ApartmentListView(FilterView):
    model = Apartment
    filterset_class = ApartmentFilters
    paginate_by = 20
    ordering = '-created_at'
    template_name = 'apartments.html'


class ApartmentCreateView(CreateView):
    model = Apartment
    form_class = ApartmentForm
    template_name = 'add.html'
    success_url = reverse_lazy('apartments')

    # def form_valid(self, form):
    #     form.instance.owner = self.request.user
    #     return super().form_valid(form)


class ApartmentUpdateView(UpdateView):
    model = Apartment
    form_class = ApartmentForm
    template_name = 'add.html'
    success_url = reverse_lazy('apartments')


class ApartmentDeleteView(PageHeaderMixin, DeleteView):
    model = Apartment
    template_name = 'delete.html'
    page_title = 'apartments'
    success_url = reverse_lazy('apartments')


# public

class HomeView(TemplateView):
    template_name = 'index.html'


class SuccessView(TemplateView):
    template_name = 'success.html'


class PublicApartmentListView(FilterView):
    model = Apartment
    filterset_class = ApartmentFilters
    paginate_by = 10
    ordering = '-created_at'
    template_name = 'properties.html'


class PublicApartmentView(DetailView):
    model = Apartment
    template_name = 'single_property.html'

    def get_context_data(self, **kwargs):
        context = super(PublicApartmentView, self).get_context_data()
        a = Booking.objects.filter(user=self.request.user, apartment=self.object.pk)
        context['status'] = True if a else False

        return context


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact.html'
    success_message = "Contact successfully submitted."
    success_url = reverse_lazy('home')
