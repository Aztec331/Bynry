from rest_framework import serializers
from .models import Supplier


class SupplierSerializer(serializers.ModelSerializer):
    """
    Serializer for Supplier.
    Used inside low-stock alerts API response.
    """

    class Meta:
        model = Supplier
        fields = [
            "id",
            "name",
            "contact_email",
        ]
