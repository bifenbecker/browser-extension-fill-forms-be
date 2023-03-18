from rest_framework.viewsets import ModelViewSet
from customers.serializers import CustomerSettingsSerializer, CustomerSettingsCreateSerializer
from customers.models import CustomerDictSettings


class CustomerSettingsViewSet(ModelViewSet):
    queryset = CustomerDictSettings.objects.all()
    serializer_class = CustomerSettingsSerializer

    def get_object(self):
        obj = self.filter_queryset(self.get_queryset()).filter(customer=self.request.user).last()
        self.check_object_permissions(self.request, obj)
        return obj

    def get_serializer_class(self, *args, **kwargs):
        if self.action == 'create':
            return CustomerSettingsCreateSerializer
        elif self.action == 'retrieve':
            return self.serializer_class
        return self.serializer_class

    def create(self, request, *args, **kwargs):
        request.data.update({
            "customer": request.user.id,
        })
        return super().create(request, *args, **kwargs)