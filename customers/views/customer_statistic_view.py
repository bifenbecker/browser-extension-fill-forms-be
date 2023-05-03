from rest_framework import viewsets
from customers.serializers import CustomerStatisticSerializer, CustomerStatisticCreateSerializer
from customers.models import CustomerStatistic, CustomerDictSettings


class CustomerStatisticViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerStatisticCreateSerializer

    def get_queryset(self):
        return CustomerStatistic.objects.filter(settings__customer=self.request.user)

    def create(self, request, *args, **kwargs):
        request.data.update({
            "settings": CustomerDictSettings.objects.filter(customer=request.user).first().id,
        })
        return super().create(request, *args, **kwargs)
