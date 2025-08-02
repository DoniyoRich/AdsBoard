from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

from config.constants import USER_ROLE


class CustomUserManager(BaseUserManager):
    """
    Кастомный менеджер пользователя.
    """
    def _create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email должен быть установлен")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)


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

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
