from djoser.serializers import UserCreateSerializer
from djoser.conf import settings

class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = (
            settings.LOGIN_FIELD,
            "password",
        )

    def perform_create(self, validated_data):
        validated_data.update({
            "username": validated_data.get("email").split("@")[0]
        })
        return super().perform_create(validated_data)
