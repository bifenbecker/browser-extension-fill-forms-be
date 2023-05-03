from django.urls import path, include
from customers.views import CustomerSettingsViewSet, CustomerAddressesView, CustomerPaymentsView, \
    CustomerSettingsInitView, CustomerStatisticViewSet

urlpatterns = [
    path(r"auth/", include("djoser.urls")),
    path(r"auth/", include("djoser.urls.jwt")),
    path(r"customer/settings/init/", CustomerSettingsInitView.as_view()),
    path(r"customer/settings/", CustomerSettingsViewSet.as_view({
        'get': 'retrieve',
        'post': 'create',
        'patch': 'partial_update',
        'delete': 'destroy',
    })),
    path(r"customer/settings/address/", CustomerAddressesView.as_view({
        'get': 'retrieve',
        'post': 'create',
        'patch': 'partial_update',
        'delete': 'destroy',
    })),
    path(r"customer/settings/payment/", CustomerPaymentsView.as_view({
        'get': 'retrieve',
        'post': 'create',
        'patch': 'partial_update',
        'delete': 'destroy',
    })),
    path(r"customer/statistic/", CustomerStatisticViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }))
]
