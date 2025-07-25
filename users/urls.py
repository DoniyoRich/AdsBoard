from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from users.apps import UsersConfig
from users.views import (PasswordRecoveryConfirmView, PasswordResetView,
                         UserDeleteAPIView, UserDetailAPIView, UserListAPIView,
                         UserRegisterView, UserUpdateAPIView)

app_name = UsersConfig.name

urlpatterns = [
    path('reset-password/', PasswordResetView.as_view(), name='password_reset'),
    path('reset_password_confirm/', PasswordRecoveryConfirmView.as_view(), name='password_recovery_confirm'),

    path('login/', TokenObtainPairView.as_view(permission_classes=[AllowAny]), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=[AllowAny]), name='token_refresh'),

    path('register/', UserRegisterView.as_view(), name='register'),
    path('', UserListAPIView.as_view(), name='users_list'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_update'),
    path('detail/<int:pk>/', UserDetailAPIView.as_view(), name='user_detail'),
    path('delete/<int:pk>/', UserDeleteAPIView.as_view(), name='user_delete'),
]
