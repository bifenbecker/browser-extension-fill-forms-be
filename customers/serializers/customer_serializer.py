from rest_framework.serializers import ModelSerializer
from customers.models import CustomUser


class CustomerSerializer(ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ("email", "id")
