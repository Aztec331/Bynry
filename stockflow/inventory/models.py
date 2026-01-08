from django.db import models
from companies.models import Company

class Warehouse(models.Model):
    """
    Represents a physical warehouse owned by a company.

    A company can have multiple warehouses.
    Inventory is tracked per warehouse.
    """

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="warehouses",
        help_text="Company that owns this warehouse"
    )

    name = models.CharField(
        max_length=255,
        help_text="Warehouse name (unique per company)"
    )

    location = models.CharField(
        max_length=255,
        blank=True,
        help_text="Optional warehouse location"
    )

    class Meta:
        unique_together = ("company", "name")

    def __str__(self):
        return f"{self.name} - {self.company.name}"
    
class Inventory(models.Model):
    """
    Represents stock of a product in a specific warehouse.

    Product × Warehouse = Inventory
    """

    product = models.ForeignKey(
        "products.Product",
        on_delete=models.CASCADE,
        related_name="inventory_records"
    )

    warehouse = models.ForeignKey(
        Warehouse,
        on_delete=models.CASCADE,
        related_name="inventory_records"
    )

    quantity = models.IntegerField(
        default=0,
        help_text="Current available stock"
    )

    class Meta:
        unique_together = ("product", "warehouse")

    def __str__(self):
        return f"{self.product.name} @ {self.warehouse.name}"
    
class InventoryChange(models.Model):
    """
    Tracks inventory history for auditing and analytics.

    Used to:
    - Track stock updates
    - Understand inventory movements
    """

    inventory = models.ForeignKey(
        Inventory,
        on_delete=models.CASCADE,
        related_name="changes"
    )

    change = models.IntegerField(
        help_text="Positive or negative stock change"
    )

    reason = models.CharField(
        max_length=255,
        help_text="Reason for inventory change"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="When the inventory change occurred"
    )


