from django.contrib import admin
from . import models


class ShippingAddressInline(admin.TabularInline):
    model = models.ShippingAddress
    extra = 1


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'email']
    inlines = [
        ShippingAddressInline
    ]


admin.site.register(models.Profile, ProfileAdmin)
admin.site.register(models.ShippingAddress)
