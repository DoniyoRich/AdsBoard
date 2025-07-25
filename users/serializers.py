from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ModelSerializer

from users.models import CustomUser


class UserSerializer(ModelSerializer):
    """
    Сериализатор всех полей модели пользователя.
    """

    class Meta:
        model = CustomUser
        fields = "__all__"

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)


class UserSerializerLimited(ModelSerializer):
    """
    Сериализатор определенных полей модели пользователя.
    """

    class Meta:
        model = CustomUser
        fields = ("id", "first_name", "last_name", "email", "phone", "role")
