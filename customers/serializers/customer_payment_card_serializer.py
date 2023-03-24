from rest_framework import serializers
from customers.models import CustomerPaymentCardMethod


class CustomerPaymentCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerPaymentCardMethod
        exclude = ("customer_settings", "id")
