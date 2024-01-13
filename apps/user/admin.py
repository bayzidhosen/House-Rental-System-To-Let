from django.contrib import admin
from django.contrib.admin import AdminSite

from apps.user.models import Staff, Customer, CustomUser, OtpToken, HouseOwner


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'email', 'username']


class HouseOwnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'username']


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'username']


admin.site.register(CustomUser, UserAdmin)
admin.site.register(Staff)
admin.site.register(HouseOwner, HouseOwnerAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(OtpToken)

