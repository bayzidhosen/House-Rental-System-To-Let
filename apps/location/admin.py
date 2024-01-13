from django.contrib import admin

from apps.location.models import Division, District, UpazilaOrThana, UnionOrWard

# Register your models here.
admin.site.register(Division)
admin.site.register(District)
admin.site.register(UpazilaOrThana)
admin.site.register(UnionOrWard)
