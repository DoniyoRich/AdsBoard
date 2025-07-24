from rest_framework.serializers import ModelSerializer

from users.models import CustomUser


class UserSerializer(ModelSerializer):
    """
    Сериализатор всех полей модели пользователя.
    """

    class Meta:
        model = CustomUser
        fields = "__all__"


class UserSerializerLimited(ModelSerializer):
    """
    Сериализатор определенных полей модели пользователя.
    """

    class Meta:
        model = CustomUser
        fields = ("id", "first_name", "last_name", "email", "phone", "role")
