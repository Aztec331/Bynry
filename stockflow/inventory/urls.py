from django.urls import path
from .views import LowStockAlertsAPIView

urlpatterns = [
    path(
        "companies/<int:company_id>/alerts/low-stock/",LowStockAlertsAPIView.as_view(),name="low-stock-alerts",
    ),
]
