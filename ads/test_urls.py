import pytest
from django.urls import reverse


@pytest.mark.django_db(transaction=True)
def test_api_ads_list(api_client):
    """
    Тестирование эндпойнта получения списка всех объявлений.
    """
    url = reverse('ads:ads_total_list')
    response = api_client.get(url)
    assert response.status_code == 200
    assert len(response.json()) >= 0


@pytest.mark.django_db(transaction=True)
def test_api_create_and_delete(api_client, user):
    """
    Тестирование эндпойнта создания и удаления объявления.
    """
    api_client.force_authenticate(user=user)

    create_data = {'title': 'API Test', 'price': 50}
    create_url = reverse('ads:ad_create')
    create_response = api_client.post(create_url, create_data, format='json')

    assert create_response.status_code == 201

    ad_id = create_response.json()['id']
    delete_url = reverse('ads:ad_delete', kwargs={'pk': ad_id})
    delete_response = api_client.delete(delete_url)

    assert delete_response.status_code == 204


@pytest.mark.django_db(transaction=True)
def test_api_feedback_list(api_client):
    """
    Тестирование эндпойнта получения списка всех комментариев.
    """
    url = reverse('ads:feedbacks_list')
    response = api_client.get(url)
    assert response.status_code == 200
    assert len(response.json()) >= 0


@pytest.mark.django_db(transaction=True)
def test_api_create_self_comment(api_client, user, ad):
    """
    Тестирование валидации создания комментария самому себе.
    """
    api_client.force_authenticate(user=user)
    feedback_data = {"text": "Какой то комментарий", "author": user.id, "ad": ad.id}
    create_url = reverse('ads:feedback_create')
    create_response = api_client.post(create_url, data=feedback_data, format='json')

    assert create_response.json() == {'non_field_errors': ['Нельзя оставлять отзыв самому себе.']}
