from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.files.storage import DefaultStorage
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DetailView, FormView, ListView, DeleteView
from formtools.wizard.views import SessionWizardView

from .forms import (ProfileUpdateForm,
                    CustomProfileCreateForm, CustomSignupForm
                    )
from .models import CustomUser

# Create your views here.

User = get_user_model()


class ProfileUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = ProfileUpdateForm
    template_name = 'account/add.html'
    success_url = reverse_lazy('dashboard')
    success_message = "Profile was updated successfully"

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class ProfileDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = 'user.view_user'
    model = User
    template_name = 'account/detail.html'

    def get_object(self, queryset=None):
        return self.request.user


class RegistrationWizardView(SessionWizardView):
    file_storage = DefaultStorage()
    template_name = "account/registration.html"
    form_list = [CustomSignupForm, CustomProfileCreateForm]
    instance = None

    def get_form_instance(self, step):
        if self.instance is None:
            self.instance = User()
        return self.instance

    def done(self, form_list, **kwargs):
        self.instance.save()
        # data = {}
        # for form in form_list:
        #     data.update(**form.cleaned_data)
        # if data.get('password1', None):
        #     data.update({'password': data['password1']})
        #     data.pop('password1')
        #     data.pop('password2')
        # User.objects.create_user(**data)
        return redirect(reverse_lazy('account_login'))


# class UserUpdateWizardView(SessionWizardView):
#     file_storage = DefaultStorage()
#     template_name = "account/registration.html"
#     form_list = [CustomUserCreationForm, CustomProfileCreateForm]
#     instance = None
#
#     def get_form_initial(self, step):
#         user = User.objects.get(id=self.request.user.id)
#         user_dict = model_to_dict(user)
#         return user_dict
#
#     def get_form_instance(self, step):
#         if self.instance is None:
#             self.instance = User()
#         return self.instance
#
#     def done(self, form_list, **kwargs):
#         data = {}
#         for form in form_list:
#             data.update(**form.cleaned_data)
#         if data.get('password1', None):
#             data.update({'password': data['password1']})
#             data.pop('password1')
#             data.pop('password2')
#         User.objects.create_user(**data)
#         return redirect(reverse_lazy('account_login'))


class UserListView(LoginRequiredMixin, ListView):
    # permission_required = 'configuration.view_unit'
    model = CustomUser
    template_name = 'list.html'
    paginate_by = 10
    ordering = '-id'


class UserCreateView(FormView):
    # permission_required = 'configuration.add_unit'
    model = User
    form_class = CustomSignupForm
    success_url = reverse_lazy('account_login')
    template_name = 'account/signup.html'

    def form_valid(self, form):
        self.user = form.save(self.request)
        return super().form_valid(form)


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy('user_list')
    template_name = 'delete.html'
