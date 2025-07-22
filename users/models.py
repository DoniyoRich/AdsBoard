from django.contrib.auth.models import AbstractUser
from django.db import models

from config.constants import USER_ROLE


class CustomUser(AbstractUser):
    """
    Модель кастомного Пользователя.
    """
    username = None
    first_name = models.CharField(max_length=30, verbose_name="Имя", blank=True, null=True)
    last_name = models.CharField(max_length=30, verbose_name="Фамилия", blank=True, null=True)
    phone = models.CharField(max_length=30, verbose_name="Номер телефона", blank=True, null=True)
    email = models.EmailField(unique=True, verbose_name="e-mail")
    role = models.CharField(max_length=20, choices=USER_ROLE)
    image = models.ImageField(upload_to="users/avatars/", default="user", verbose_name="Аватар", blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
