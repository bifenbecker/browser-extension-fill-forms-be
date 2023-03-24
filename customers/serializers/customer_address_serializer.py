from rest_framework import serializers
from customers.models import CustomerAddress


class CustomerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerAddress
        exclude = ("customer_settings", "id")
