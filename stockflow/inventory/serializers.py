from rest_framework import serializers
from .models import Inventory

class InventorySerializer(serializers.ModelSerializer):
    """
    Serializer for Inventory model.
    Used in low-stock alerts response.
    """

    warehouse_name = serializers.CharField(
        source="warehouse.name",
        read_only=True
    )

    class Meta:
        model = Inventory
        fields = [
            "id",
            "warehouse",
            "warehouse_name",
            "quantity"
        ]

class LowStockAlertSerializer(serializers.Serializer):
    """
    Serializer for low-stock alert response.
    This is NOT tied to a model (computed response).
    """

    product_id = serializers.IntegerField()
    product_name = serializers.CharField()
    sku = serializers.CharField()

    warehouse_id = serializers.IntegerField()
    warehouse_name = serializers.CharField()

    current_stock = serializers.IntegerField()
    threshold = serializers.IntegerField()
    days_until_stockout = serializers.IntegerField(allow_null=True)

    supplier = serializers.DictField()

