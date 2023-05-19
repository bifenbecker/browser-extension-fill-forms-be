from rest_framework import serializers
from customers.models import CustomerStatistic, FillField
from customers.serializers import CustomerSettingsSerializer


class FillFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = FillField
        fields = "__all__"


class FillFieldCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FillField
        exclude = ("statistic", )


class CustomerStatisticSerializer(serializers.ModelSerializer):
    fields = serializers.ListSerializer(child=FillFieldSerializer())

    class Meta:
        model = CustomerStatistic
        fields = "__all__"


class CustomerStatisticCreateSerializer(serializers.ModelSerializer):
    fields = serializers.ListSerializer(child=FillFieldCreateSerializer())

    class Meta:
        model = CustomerStatistic
        fields = "__all__"

    def create(self, validated_data):
        fields_data = validated_data.pop("fields")
        statistic = CustomerStatistic.objects.create(**validated_data)
        fields = []
        for field in fields_data:
            fields.append(FillField(**field, statistic=statistic))
        FillField.objects.bulk_create(fields)
        return statistic


