import pytest
from django.core.exceptions import ValidationError

from ads.models import Ad, Feedback


@pytest.mark.django_db(transaction=True)
def test_create_ad(user, ad):
    """
    Тест создания объявления.
    """

    assert ad.title == 'Продам телефон Samsung'
    assert ad.price == 25000
    assert ad.description == 'Рабочий телефон, использовался один год'
    assert ad.author == user
    assert str(ad) == "Объявление: Продам телефон Samsung. Цена: 25000 р."


@pytest.mark.django_db(transaction=True)
def test_ad_price_validation(user):
    """
    Тест валидации цены (не может быть меньше 1).
    """

    with pytest.raises(ValidationError):
        ad = Ad(title='Невалидный товар', price=0, author=user)
        ad.full_clean()


@pytest.mark.django_db(transaction=True)
def test_multiple_ads_creation(user):
    """
    Тест создания нескольких объявлений.
    """
    ads_data = [
        {'title': 'Товар 1', 'price': 1000},
        {'title': 'Товар 2', 'price': 2000},
        {'title': 'Товар 3', 'price': 3000},
    ]

    for data in ads_data:
        Ad.objects.create(**data, author=user)

    assert Ad.objects.count() == 3
    assert Ad.objects.filter(price__gt=1500).count() == 2


@pytest.mark.django_db(transaction=True)
def test_create_feedback(feedback_data):
    """
    Тест создания комментария.
    """
    feedback = Feedback.objects.create(**feedback_data)

    assert feedback.text == 'Какой то комментарий'
