from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

urlpatterns = [
    path('applied/', login_required(views.MyApplyView.as_view()), name='my_apply'),
]
