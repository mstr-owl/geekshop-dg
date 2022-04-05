import json
from django.core.management.base import BaseCommand

from authapp.models import User
from mainapp.models import ProductCategories, Product


def load_from_json(file_name):
    with open(file_name, mode='r', encoding='utf-8') as infile:

        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        User.objects.create_superuser(username='superusermen',email='admin@mail.ru',password='987456Adm')
        categories = load_from_json('mainapp/fixtures/category')

        ProductCategories.objects.all().delete()
        for category in categories:
            cat = category.get('fields')
            cat['id'] = category.get('pk')
            new_category = ProductCategories(**cat)
            new_category.save()

        products = load_from_json('mainapp/fixtures/products')

        Product.objects.all().delete()
        for product in products:
            prod = product.get('fields')
            category = prod.get('category')
            _category = ProductCategories.objects.get(id=category)
            prod['category'] =_category
            new_category = Product(**prod)
            new_category.save()