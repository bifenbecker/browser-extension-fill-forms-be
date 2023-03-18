from rest_framework import serializers
from customers.models import CustomerDictSettings


class CustomerSettingsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerDictSettings
        fields = (
            "email_address",
            "first_name",
            "last_name",
            "mobile_number",
            "isAgreeSendMessagesOnEmail",
            "customer",
        )
