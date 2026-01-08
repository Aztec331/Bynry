from django.contrib import admin
from .models import Warehouse, Inventory, InventoryChange

@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "company", "location")
    search_fields = ("name", "company__name")

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "warehouse", "quantity")
    list_filter = ("warehouse",)

@admin.register(InventoryChange)
class InventoryChangeAdmin(admin.ModelAdmin):
    list_display = ("inventory", "change", "reason", "created_at")
    ordering = ("-created_at",)
