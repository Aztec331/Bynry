from django.contrib import admin
from .models import Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    """
    Admin configuration for Company model.
    """

    list_display = ("id", "name", "created_at")
    search_fields = ("name",)
    ordering = ("name",)
