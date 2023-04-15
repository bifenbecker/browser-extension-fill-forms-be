
from rest_framework import viewsets
from django.http import Http404

from customers.models import CustomerAddress
from customers.serializers import CustomerAddressSerializer


class CustomerAddressesView(viewsets.ModelViewSet):
    queryset = CustomerAddress.objects.all()
    serializer_class = CustomerAddressSerializer

    def get_queryset(self):
        return CustomerAddress.objects.all()

    def filter_queryset(self, queryset):
        return queryset.filter(customer_settings__customer=self.request.user, is_active=True).first()

    def get_object(self):
        queryset = self.get_queryset()
        obj = self.filter_queryset(queryset)
        if not obj:
            raise Http404
        self.check_object_permissions(self.request, obj)
        return obj
