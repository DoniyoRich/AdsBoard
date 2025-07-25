from django.contrib.auth.hashers import make_password
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from rest_framework import status
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from config import settings
from users.models import CustomUser
from users.paginators import UserPaginator
from users.permissions import IsAdmin, IsOwner
from users.serializers import UserSerializer, UserSerializerLimited


class UserRegisterView(CreateAPIView):
    """
    API регистрации пользователя.
    """
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserListAPIView(ListAPIView):
    """
    API получения списка пользователей.
    """
    serializer_class = UserSerializerLimited
    queryset = CustomUser.objects.all()
    pagination_class = UserPaginator
    permission_classes = [IsAdmin | IsOwner]


class UserDetailAPIView(RetrieveAPIView):
    """
    API получения одного пользователя.
    """
    serializer_class = UserSerializerLimited
    queryset = CustomUser.objects.all()
    permission_classes = [IsAdmin | IsOwner]


class UserUpdateAPIView(UpdateAPIView):
    """
    API редактирования профиля пользователя.
    """
    serializer_class = UserSerializerLimited
    queryset = CustomUser.objects.all()
    permission_classes = [IsOwner]


class UserDeleteAPIView(DestroyAPIView):
    """
    API удаления профиля пользователя.
    """
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [IsAdmin]


class PasswordResetView(APIView):
    """
    API сброса пароля.
    """
    permission_classes = []

    def post(self, request):

        email = request.data.get('email')

        if not email:
            return Response({'error': 'Необходимо предоставить email'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return Response({'error': 'Пользователь с таким email не найден'}, status=status.HTTP_404_NOT_FOUND)

        token = PasswordResetTokenGenerator().make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))

        reset_url = request.build_absolute_uri(
            f"/reset-password-confirm/?uid={uid}&token={token}"
        )

        send_mail(
            'Сброс пароля',
            f'Для сброса пароля отправьте POST-запрос на: {reset_url}\n'
            f'С параметрами: uid, token, new_password',
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )

        return Response({'reset_url': reset_url}, status=status.HTTP_200_OK)


class PasswordRecoveryConfirmView(APIView):
    """
    Подтверждение восстановления пароля.
    """
    permission_classes = []

    def post(self, request):
        uid = request.data.get('uid')
        token = request.data.get('token')
        new_password = request.data.get('new_password')

        if not all([uid, token, new_password]):
            return Response({'error': 'Необходимо предоставить uid, token и new_password'},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            uid = force_str(urlsafe_base64_decode(uid))
            user = CustomUser.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            user = None

        if user and PasswordResetTokenGenerator().check_token(user, token):
            user.password = make_password(new_password)
            user.save()
            return Response({'detail': 'Пароль успешно сброшен'}, status=status.HTTP_200_OK)

        return Response({'error': 'Некорректный token или uid'}, status=status.HTTP_400_BAD_REQUEST)
