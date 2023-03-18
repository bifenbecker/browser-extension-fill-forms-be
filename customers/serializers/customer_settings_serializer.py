from rest_framework import serializers
from customers.models import CustomerDictSettings
from customers.serializers import CustomerSerializer


class CustomerSettingsSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True, many=False)
    full_name = serializers.SerializerMethodField()

    def get_full_name(self, obj):
        return obj.get_full_name_customer()

    class Meta:
        model = CustomerDictSettings
        fields = (
            "customer",
            "email_address",
            "first_name",
            "last_name",
            "mobile_number",
            "isAgreeSendMessagesOnEmail",
            "full_name"
        )
