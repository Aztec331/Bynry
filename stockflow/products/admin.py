from django.contrib import admin
from .models import Product, ProductBundle

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Admin configuration for Product.
    """

    list_display = (
        "id",
        "name",
        "sku",
        "company",
        "product_type",
        "low_stock_threshold",
    )
    search_fields = ("name", "sku")
    list_filter = ("product_type", "company")

@admin.register(ProductBundle)
class ProductBundleAdmin(admin.ModelAdmin):
    list_display = ("bundle", "item", "quantity")

