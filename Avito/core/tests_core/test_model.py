from django.test import TestCase
from core.models import CategoriesAd


class CategoriesAdTestModel(TestCase):
    def setUp(self):
        CategoriesAd.objects.create(name='Велосипеды')  

    def test_name_label(self):
        """
        тест проверяет соответствие атрибутов класса модели
        """
        cat_ad = CategoriesAd.objects.first()
        name_cat = cat_ad._meta.get_field('name').verbose_name   
        self.assertEqual(name_cat, 'name')

    def test_str_method(self):
        """
        проверка __str__ модели
        """
        cat_ad = CategoriesAd.objects.first()
        name_cat = '{}'.format(cat_ad.name)
        self.assertEquals(name_cat, str(cat_ad))

