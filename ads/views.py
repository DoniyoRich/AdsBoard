from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import AllowAny

from ads.models import Ad, Feedback
from ads.paginators import AdPaginator
from ads.serializers import AdSerializer, FeedbackSerializer
from users.permissions import IsAdmin, IsOwner


# Набор API для объявлений
class AdsTotalListAPIView(ListAPIView):
    """
    Список всех объявлений в системе.
    """
    serializer_class = AdSerializer
    pagination_class = AdPaginator
    permission_classes = [AllowAny]


class AdsUserListAPIView(ListAPIView):
    """
    Список всех объявлений определенного пользователя.
    """
    serializer_class = AdSerializer
    pagination_class = AdPaginator
    permission_classes = [IsAdmin | IsOwner]

    def get_queryset(self):
        return Ad.objects.filter(author=self.request.user)


class AdCreateAPIView(CreateAPIView):
    """
    Создание объявления.
    """
    serializer_class = AdSerializer
    permission_classes = [IsAdmin | IsOwner]


class AdDetailAPIView(RetrieveAPIView):
    """
    Просмотр обявления.
    """
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    permission_classes = [IsAdmin | IsOwner]


class AdUpdateAPIView(UpdateAPIView):
    """
    Редактирование объявления.
    """
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    permission_classes = [IsAdmin | IsOwner]


class AdDeleteAPIView(DestroyAPIView):
    """
    Удаление объявления.
    """
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    permission_classes = [IsAdmin | IsOwner]


# Набор API для отзывов
class FeedbackListAPIView(ListAPIView):
    """
    Список всех отзывов.
    """
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    pagination_class = AdPaginator


class FeedbackCreateAPIView(CreateAPIView):
    """
    Создание отзыва.
    """
    serializer_class = FeedbackSerializer
    permission_classes = [IsAdmin | IsOwner]


class FeedbackDetailAPIView(RetrieveAPIView):
    """
    Просмотр отзыва.
    """
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    permission_classes = [IsAdmin | IsOwner]


class FeedbackUpdateAPIView(UpdateAPIView):
    """
    Редактирование отзыва.
    """
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    permission_classes = [IsAdmin | IsOwner]


class FeedbackDeleteAPIView(DestroyAPIView):
    """
    Удаление отзыва.
    """
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    permission_classes = [IsAdmin | IsOwner]
