from django.contrib import admin
from .models import Supplier, ProductSupplier


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    """
    Admin configuration for Supplier.
    """

    list_display = ("id", "name", "company", "contact_email")
    search_fields = ("name", "contact_email")
    list_filter = ("company",)

@admin.register(ProductSupplier)
class ProductSupplierAdmin(admin.ModelAdmin):
    list_display = ("product", "supplier")
