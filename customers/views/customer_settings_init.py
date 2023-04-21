from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from customers.models import CustomerAddress, CustomerPaymentCardMethod, CustomerDictSettings


class CustomerSettingsInitView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = self.request.user
        settings = CustomerDictSettings.objects.create(customer=user)
        CustomerAddress.objects.create(customer_settings=settings, is_active=True)
        CustomerPaymentCardMethod.objects.create(customer_settings=settings, is_active=True)
        return Response(status=HTTP_201_CREATED)
