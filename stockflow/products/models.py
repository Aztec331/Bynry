from django.db import models
from companies.models import Company

class Product(models.Model):
    """
    Represents a product sold or managed by a company.

    Key points:
    - SKU must be unique across the platform
    - Products belong to a company
    - Products can exist in multiple warehouses (via Inventory)
    - Used in low-stock alerts (Part 3)
    """

    PRODUCT_TYPES = (
        ("regular", "Regular"),
        ("fragile", "Fragile"),
        ("perishable", "Perishable"),
    )

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="products",
        help_text="Company that owns this product"
    )

    name = models.CharField(
        max_length=255,
        help_text="Product name"
    )

    sku = models.CharField(
        max_length=100,
        unique=True,
        help_text="Globally unique SKU"
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Product price (decimal for accuracy)"
    )

    product_type = models.CharField(
        max_length=50,
        choices=PRODUCT_TYPES,
        help_text="Used to determine low-stock thresholds"
    )

    low_stock_threshold = models.IntegerField(
        default=10,
        help_text="Minimum stock before alert is triggered"
    )

    has_recent_sales = models.BooleanField(
        default=False,
        help_text="Used to filter alerts (Part 3 rule)"
    )

    daily_sales_rate = models.FloatField(
        default=0,
        help_text="Average daily sales, used to estimate stockout"
    )

    def __str__(self):
        return f"{self.name} ({self.sku})"

class ProductBundle(models.Model):
    """
    Represents a bundle made of multiple products.

    Example:
    - Bundle: 'Office Starter Kit'
    - Contains: Chair (1), Desk (1), Lamp (2)
    """

    bundle = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="bundle_items",
        help_text="The main bundled product"
    )

    item = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="included_in",
        help_text="Product included in the bundle"
    )

    quantity = models.IntegerField(
        help_text="Quantity of item in the bundle"
    )

    class Meta:
        unique_together = ("bundle", "item")

    def __str__(self):
        return f"{self.bundle.name} -> {self.item.name} ({self.quantity})"
