from django.db import models

class Company(models.Model):
    """
    Represents a business using the StockFlow platform.

    A Company:
    - Owns warehouses
    - Owns products
    - Receives low-stock alerts (Part 3)
    """

    name = models.CharField(
        max_length=255,
        unique=True,
        help_text="Unique company name"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Timestamp when the company was created"
    )

    def __str__(self):
        return self.name
