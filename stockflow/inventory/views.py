from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from inventory.models import Inventory
from suppliers.models import ProductSupplier


class LowStockAlertsAPIView(APIView):
    """
    Returns low-stock alerts for a given company.

    Business rules:
    - Threshold varies per product
    - Only products with recent sales are considered
    - Handles multiple warehouses
    - Includes supplier info for reordering
    """

    def get(self, request, company_id):
        alerts = []

        inventory_qs = Inventory.objects.select_related(
            "product",
            "warehouse",
            "warehouse__company",
        ).filter(
            warehouse__company_id=company_id,
            product__has_recent_sales=True
        )

        for inventory in inventory_qs:
            product = inventory.product
            warehouse = inventory.warehouse

            # Check low stock condition
            if inventory.quantity < product.low_stock_threshold:
                # Estimate days until stockout
                if product.daily_sales_rate > 0:
                    days_until_stockout = int(
                        inventory.quantity / product.daily_sales_rate
                    )
                else:
                    days_until_stockout = None

                # Get supplier (first one for simplicity)
                supplier_link = ProductSupplier.objects.filter(
                    product=product
                ).select_related("supplier").first()

                supplier_data = None
                if supplier_link:
                    supplier = supplier_link.supplier
                    supplier_data = {
                        "id": supplier.id,
                        "name": supplier.name,
                        "contact_email": supplier.contact_email,
                    }

                alerts.append({
                    "product_id": product.id,
                    "product_name": product.name,
                    "sku": product.sku,
                    "warehouse_id": warehouse.id,
                    "warehouse_name": warehouse.name,
                    "current_stock": inventory.quantity,
                    "threshold": product.low_stock_threshold,
                    "days_until_stockout": days_until_stockout,
                    "supplier": supplier_data,
                })

        return Response(
            {
                "alerts": alerts,
                "total_alerts": len(alerts),
            },
            status=status.HTTP_200_OK
        )
