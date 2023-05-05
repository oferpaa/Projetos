from django.contrib import admin
from . import models


class VariationInline(admin.TabularInline):
    model = models.Variation
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_price_format', 'get_price_promo_format']
    inlines = [
        VariationInline
    ]


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Variation)
