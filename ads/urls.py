from django.urls import path

from ads.apps import AdsConfig
from ads.views import AdsTotalListAPIView, AdsUserListAPIView, AdCreateAPIView, AdUpdateAPIView, AdDetailAPIView, \
    AdDeleteAPIView, FeedbackListAPIView, FeedbackCreateAPIView, FeedbackUpdateAPIView, FeedbackDetailAPIView, \
    FeedbackDeleteAPIView

app_name = AdsConfig.name

urlpatterns = [
    # эндпойнты для объявлений
    path("", AdsTotalListAPIView.as_view(), name="ads_total_list"),
    path("user/", AdsUserListAPIView.as_view(), name="ads_user_list"),
    path("create/", AdCreateAPIView.as_view(), name="ad_create"),
    path("update/<int:pk>/", AdUpdateAPIView.as_view(), name="ad_update"),
    path("detail/<int:pk>/", AdDetailAPIView.as_view(), name="ad_detail"),
    path("delete/<int:pk>/", AdDeleteAPIView.as_view(), name="ad_delete"),

    # эндпойнты для отзывов
    path("feedbacks/", FeedbackListAPIView.as_view(), name="feedbacks_list"),
    path("feedback/create/", FeedbackCreateAPIView.as_view(), name="feedback_create"),
    path("feedback/update/<int:pk>/", FeedbackUpdateAPIView.as_view(), name="feedback_update"),
    path("feedback/detail/<int:pk>/", FeedbackDetailAPIView.as_view(), name="feedback_detail"),
    path("feedback/delete/<int:pk>/", FeedbackDeleteAPIView.as_view(), name="feedback_delete"),
]
