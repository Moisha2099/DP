from django.contrib import admin

from general.models import UserProfile, Type_service, Order

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Type_service)
admin.site.register(Order)