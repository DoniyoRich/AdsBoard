from rest_framework import filters
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
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Ad.objects.all() \
            .order_by('-created_at') \
            .select_related('author') \
            .prefetch_related('feedbacks')


class AdsUserListAPIView(ListAPIView):
    """
    Список всех объявлений определенного пользователя.
    """
    serializer_class = AdSerializer
    pagination_class = AdPaginator
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
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


# Набор API для комментариев
class FeedbackListAPIView(ListAPIView):
    """
    Список всех комментариев.
    """
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    pagination_class = AdPaginator
    permission_classes = [AllowAny]


class FeedbackUserListAPIView(ListAPIView):
    """
    Список всех комментариев определенного пользователя.
    """
    serializer_class = FeedbackSerializer
    pagination_class = AdPaginator
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Feedback.objects.filter(author=self.request.user)


class FeedbackCreateAPIView(CreateAPIView):
    """
    Создание комментария.
    """
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FeedbackDetailAPIView(RetrieveAPIView):
    """
    Просмотр комментария.
    """
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    permission_classes = [IsAuthenticated & (IsAdmin | IsOwner)]


class FeedbackUpdateAPIView(UpdateAPIView):
    """
    Редактирование комментария.
    """
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    permission_classes = [IsAuthenticated & (IsAdmin | IsOwner)]


class FeedbackDeleteAPIView(DestroyAPIView):
    """
    Удаление комментария.
    """
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    permission_classes = [IsAuthenticated & (IsAdmin | IsOwner)]
