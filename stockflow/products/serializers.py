from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for Product model.
    Used in low-stock alerts response.
    """

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "sku",
            "price",
            "product_type",
            "low_stock_threshold",
            "daily_sales_rate",
        ]
