from rest_framework import serializers
from customers.models import CustomerDictSettings
from customers.serializers import CustomerSerializer, CustomerAddressSerializer, CustomerPaymentCardSerializer


class CustomerSettingsSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True, many=False)
    addresses = CustomerAddressSerializer(read_only=True, many=True)
    payment_cards = CustomerPaymentCardSerializer(read_only=True, many=True)
    full_name = serializers.SerializerMethodField()

    def get_full_name(self, obj):
        return obj.get_full_name_customer()

    class Meta:
        model = CustomerDictSettings
        fields = (
            "customer",
            "addresses",
            "payment_cards",
            "email_address",
            "first_name",
            "last_name",
            "mobile_number",
            "isAgreeSendMessagesOnEmail",
            "full_name"
        )
