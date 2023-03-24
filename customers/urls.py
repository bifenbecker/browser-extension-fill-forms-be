from django.urls import path, include
from customers.views import CustomerSettingsViewSet

urlpatterns = [
    path(r"auth/", include("djoser.urls")),
    path(r"auth/", include("djoser.urls.jwt")),
    path(r"customer/settings/", CustomerSettingsViewSet.as_view({
        'get': 'retrieve',
        'post': 'create',
        'patch': 'partial_update',
        'delete': 'destroy',
    }))
]
