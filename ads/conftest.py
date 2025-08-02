import pytest
from django.conf import settings
from django.test import Client
from rest_framework.test import APIClient

from ads.models import Ad
from users.models import CustomUser


@pytest.fixture(scope='session')
def django_db_setup():
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test_db.sqlite3',
        'ATOMIC_REQUESTS': False,
    }


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user():
    return CustomUser.objects.create_user(email='test@example.com', password='123')


@pytest.fixture
def ad(user):
    return Ad.objects.create(
        title='Продам телефон Samsung',
        price=25000,
        description='Рабочий телефон, использовался один год',
        author=user
    )


@pytest.fixture
def feedback_data(user, ad):
    return {'text': 'Какой то комментарий', 'author': user, 'ad': ad}
