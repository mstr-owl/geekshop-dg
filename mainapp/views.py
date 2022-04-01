import os
import json


from django.shortcuts import render

MODULE_DIR = os.path.dirname(__file__)

def read_file(name):
    file_path = os.path.join(MODULE_DIR, name)
    return json.load(open(file_path, encoding='utf-8'))

def index(request):
    content = {
        'title': 'Geekshop'
    }
    return render(request, 'mainapp/index.html', content)

def products(request):

    products = read_file('fixtures/goods.json')
    categories = read_file('fixtures/categories.json')

    # categories = [
    #     {'name':'Новинки'},
    #     {'name':'Одежда'},
    #     {'name':'Обувь'},
    #     {'name':'Аксессуары'},
    #     {'name':'Подарки'},
    # ]
    #
    # products = [
    #     {
    #         'name': 'Худи черного цвета с монограммами adidas Originals',
    #         'price': '6 090,00',
    #         'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
    #         'image': 'vendor/img/products/Adidas-hoodie.png'
    #     },
    #     {
    #         'name': 'Синяя куртка The North Face',
    #         'price': '23 725,00',
    #         'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
    #         'image': 'vendor/img/products/Blue-jacket-The-North-Face.png'
    #     },
    #     {
    #         'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
    #         'price': '3 390,00',
    #         'description': 'Материал с плюшевой текстурой. Удобный и мягкий.',
    #         'image': 'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png'
    #     },
    #     {
    #         'name': 'Черный рюкзак Nike Heritage',
    #         'price': '2 340,00',
    #         'description': 'Плотная ткань. Легкий материал.',
    #         'image': 'vendor/img/products/Black-Nike-Heritage-backpack.png'
    #     },
    #     {
    #         'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
    #         'price': '13 590,00',
    #         'description': 'Гладкий кожаный верх. Натуральный материал.',
    #         'image': 'vendor/img/products/Black-Dr-Martens-shoes.png'
    #     },
    #     {
    #         'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
    #         'price': '2 890,00',
    #         'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
    #         'image': 'vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png'
    #     },
    # ]

    content = {
        'title': 'Geekshop - Каталог',
        'categories': categories,
        'products': products
    }
    return render(request, 'mainapp/products.html', content)

