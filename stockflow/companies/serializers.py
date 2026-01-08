from rest_framework import serializers
from .models import Company

class CompanySerializer(serializers.ModelSerializer):
    """
    Serializer for Company model.
    Used when company data needs to be exposed via API.
    """

    class Meta:
        model = Company
        fields = ["id", "name", "created_at"]
