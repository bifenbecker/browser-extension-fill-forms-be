from djoser.serializers import TokenCreateSerializer
from django.contrib.auth import get_user_model
from djoser.conf import settings

User = get_user_model()


class CustomUserLoginSerializer(TokenCreateSerializer):
    class Meta:
        model = User
        fields = (
            settings.LOGIN_FIELD,
            "password",
        )
