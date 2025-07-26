from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import AllowAny, IsAuthenticated

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
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Ad.objects.all() \
            .select_related('author') \
            .prefetch_related('feedbacks') \
            .order_by('-created_at')


class AdsUserListAPIView(ListAPIView):
    """
    Список всех объявлений определенного пользователя.
    """
    serializer_class = AdSerializer
    pagination_class = AdPaginator
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Ad.objects.filter(author=self.request.user) \
            .select_related('author') \
            .prefetch_related('feedbacks') \
            .order_by('-created_at')


class AdCreateAPIView(CreateAPIView):
    """
    Создание объявления.
    """
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class AdDetailAPIView(RetrieveAPIView):
    """
    Просмотр объявления.
    """
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    permission_classes = [IsAuthenticated & (IsAdmin | IsOwner)]


class AdUpdateAPIView(UpdateAPIView):
    """
    Редактирование объявления.
    """
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    permission_classes = [IsAuthenticated & (IsAdmin | IsOwner)]


class AdDeleteAPIView(DestroyAPIView):
    """
    Удаление объявления.
    """
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    permission_classes = [IsAuthenticated & (IsAdmin | IsOwner)]


# Набор API для отзывов
class FeedbackListAPIView(ListAPIView):
    """
    Список всех отзывов.
    """
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    pagination_class = AdPaginator
    permission_classes = [AllowAny]


class FeedbackUserListAPIView(ListAPIView):
    """
    Список всех отзывов определенного пользователя.
    """
    serializer_class = FeedbackSerializer
    pagination_class = AdPaginator
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Feedback.objects.filter(author=self.request.user)


class FeedbackCreateAPIView(CreateAPIView):
    """
    Создание отзыва.
    """
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FeedbackDetailAPIView(RetrieveAPIView):
    """
    Просмотр отзыва.
    """
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    permission_classes = [IsAuthenticated & (IsAdmin | IsOwner)]


class FeedbackUpdateAPIView(UpdateAPIView):
    """
    Редактирование отзыва.
    """
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    permission_classes = [IsAuthenticated & (IsAdmin | IsOwner)]


class FeedbackDeleteAPIView(DestroyAPIView):
    """
    Удаление отзыва.
    """
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    permission_classes = [IsAuthenticated & (IsAdmin | IsOwner)]
