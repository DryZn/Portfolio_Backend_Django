import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db(transaction=True)
class TestProjectsAPI:
    def test_list_projects(self, api_client):
        url = reverse("project-list")
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db(transaction=True)
class TestSkillsAPI:
    def test_list_skills(self, api_client):
        url = reverse("skill-list")
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db(transaction=True)
class TestContactAPI:
    def test_send_message(self, api_client):
        url = reverse("contact")
        data = {
            "name": "Test User",
            "email": "test@example.com",
            "subject": "Test Subject",
            "message": "Test message",
        }
        response = api_client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED
