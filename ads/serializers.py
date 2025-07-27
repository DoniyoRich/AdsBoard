from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from ads.models import Ad, Feedback
from users.serializers import UserSerializerLimited


class FeedbackSerializer(ModelSerializer):
    """
    Сериализатор для модели отзыва.
    """

    class Meta:
        model = Feedback
        fields = "__all__"

    def validate(self, data):
        author = data.get("author")
        ad = data.get("ad")

        if author == ad.author:
            raise serializers.ValidationError("Нельзя оставлять отзыв самому себе.")
        return data


class AdSerializer(ModelSerializer):
    """
    Сериализатор для модели объявления.
    """
    author = UserSerializerLimited(read_only=True)
    feedbacks = FeedbackSerializer(many=True, read_only=True)

    class Meta:
        model = Ad
        fields = ['id', 'title', 'price', 'description', 'created_at', 'updated_at', 'author', 'feedbacks']
