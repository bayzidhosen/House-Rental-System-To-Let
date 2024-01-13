from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

urlpatterns = [
    path('dashboard/', login_required(views.DashboardView.as_view()), name='dashboard'),

    path('dashboard/apartment/', login_required(views.ApartmentListView.as_view()), name='apartments'),
    path('dashboard/apartment/add/', login_required(views.ApartmentCreateView.as_view()), name='apartment_add'),
    path('dashboard/apartment/<int:pk>/update/', login_required(views.ApartmentUpdateView.as_view()),
         name='apartment_update'),
    path('dashboard/apartment/<int:pk>/delete/', login_required(views.ApartmentDeleteView.as_view()),
         name='apartment_delete'),

    # public
    path('', views.HomeView.as_view(), name='home'),
    path('all-properties/', views.PublicApartmentListView.as_view(), name='apartments'),
    path('contacts/', views.ContactView.as_view(), name='contacts'),

    path('apartment/<int:pk>/details/', views.PublicApartmentView.as_view(), name='single_apartments'),

]
