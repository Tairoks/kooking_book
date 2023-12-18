import pytest

from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Recipes


class RecipesTestCase(TestCase):

    @pytest.mark.django_db
    def setUp(self) -> None:
        self.client = Client()
        self.credentials = {"username": "test_user", "password": "t49q3;uGU"}
        self.user = User.objects.create_user(self.credentials)

    def add_recipe(self):
        self.client.force_login(self.user)
        self.recipe = {'title': 'test', 'cooking': 'text', 'time_cook': '15', 'slug': 'test'}
        response = Recipes.objects.create(self.recipe)
        assert response.status_code == 200

