import django_filters

from apps.house.forms import ApartmentFiltersForm
from apps.house.models import Apartment
from apps.location.models import UnionOrWard


class ApartmentFilters(django_filters.FilterSet):
    # title = django_filters.CharFilter(method='project_filter')
    union = django_filters.ModelChoiceFilter(queryset=UnionOrWard.objects.all(), label='Location')

    class Meta:
        model = Apartment
        fields = ['rent', 'room', 'floor', 'parking', 'lift', 'district', 'thana', 'union', ]
        form = ApartmentFiltersForm

    # def project_filter(self, queryset, title, value):
    #     return queryset.filter(title__icontains=value)
