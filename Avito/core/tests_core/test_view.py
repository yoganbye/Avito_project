from django.test import TestCase, Client
from django.contrib.auth.models import User
from core.models import CategoriesAd
from django.urls import reverse


class TestIndexView(TestCase):

    def test_view_correct_template(self):
        """
        тест доступен ли юрл по имени и корректный ли template
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'core/index.html')

    def test_context(self):
        """
        Проверка контекста
        """
        response = self.client.get(reverse('index'))
        self.assertTrue('title' in response.context)
        self.assertTrue(response.context['title'] == 'Главная страница')

