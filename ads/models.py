from django.core.validators import MinValueValidator
from django.db import models
from rest_framework.exceptions import ValidationError

from config import settings


class Ad(models.Model):
    """
    Модель объявления.
    """
    title = models.CharField(max_length=50, verbose_name="Название товара")
    price = models.PositiveIntegerField(verbose_name="Цена товара", validators=[MinValueValidator(1)])
    description = models.TextField(verbose_name="Описание товара", blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Автор",
                               related_name="ads")
    created_at = models.DateTimeField(verbose_name="Дата и время создания объявления", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Дата и время изменения объявления", auto_now=True)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ["-created_at"]

    def __str__(self):
        return f"Объявление: {self.title}. Цена: {self.price} р."


class Feedback(models.Model):
    """
    Модель комментарция.
    """
    text = models.TextField(verbose_name="Текст комментария", default="", blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Автор",
                               related_name="user_feedbacks")
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, verbose_name="Объявление", related_name="feedbacks")
    created_at = models.DateTimeField(verbose_name="Дата и время создания комментария", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Дата и время изменения комментария", auto_now=True)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарий"
        ordering = ["-created_at"]

    def __str__(self):
        return f"Комментарий от {self.author} на {self.ad.title}"
