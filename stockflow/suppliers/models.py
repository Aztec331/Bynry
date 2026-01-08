from django.db import models
from companies.models import Company
from products.models import Product


class Supplier(models.Model):
    """
    Represents a supplier that provides products to a company.

    Used in Part 3:
    - Low-stock alerts must include supplier info for reordering
    """

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="suppliers",
        help_text="Company this supplier works with"
    )

    name = models.CharField(
        max_length=255,
        help_text="Supplier name"
    )

    contact_email = models.EmailField(
        help_text="Email used for reordering"
    )

    def __str__(self):
        return self.name
    
class ProductSupplier(models.Model):
    """
    Many-to-many relationship between Product and Supplier.

    A product can have multiple suppliers.
    A supplier can supply multiple products.
    """

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="product_suppliers"
    )

    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        related_name="supplier_products"
    )

    class Meta:
        unique_together = ("product", "supplier")

    def __str__(self):
        return f"{self.product.name} -> {self.supplier.name}"

