from rest_framework.serializers import ModelSerializer

from ads.models import Ad, Feedback


class AdSerializer(ModelSerializer):
    """
    Сериализатор для модели объевления.
    """

    class Meta:
        model = Ad
        fields = "__all__"


class FeedbackSerializer(ModelSerializer):
    """
    Сериализатор для модели отзыва.
    """

    class Meta:
        model = Feedback
        fields = "__all__"
