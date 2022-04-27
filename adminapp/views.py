from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm, AdminCategoryAdd, AdminCategoryUpdate, \
    AdminProductAdd, AdminProductUpdate
from authapp.models import User
from django.contrib.auth.decorators import user_passes_test
from mainapp.models import ProductCategories, Product

@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'adminapp/admin.html')

@user_passes_test(lambda u: u.is_superuser)
def admin_users(request):
    context = {
        'title': 'Админка | Пользователи',
        'users': User.objects.all()
    }
    return render(request, 'adminapp/admin-users-read.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_user_create(request):
    if request.method == 'POST':
        form = UserAdminRegisterForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_users'))
        else:
            print(form.errors)
    else:
        form=UserAdminRegisterForm()
        context = {
            'title': 'Админка | Регистрация',
            'form': form
        }

    return render(request, 'adminapp/admin-users-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_user_update(request, id):
    user_select = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserAdminProfileForm(data=request.POST, instance=user_select, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_users'))
    else:
        form = UserAdminProfileForm(instance=user_select)
    context = {
         'title': 'Админка | Обновление пользователя',
         'form': form,
         'user_select': user_select
    }
    return render(request, 'adminapp/admin-users-update-delete.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_user_delete(request, id):
    user = User.objects.get(id=id)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('adminapp:admin_users'))



@user_passes_test(lambda u: u.is_superuser)
def admin_categories(request):
    context = {
        'title': 'Админка | Пользователи',
        'categories': ProductCategories.objects.all()
    }
    return render(request, 'adminapp/admin-categories-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_category_add(request):
    if request.method == 'POST':
        form = AdminCategoryAdd(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Категория успешно добавлена')
            return HttpResponseRedirect(reverse('adminapp:admin_categories'))
        else:
            messages.error(request, form.errors)
            print(form.errors)
    else:
        form = AdminCategoryAdd
    context = {
        'title': 'Админка | Добавить категорию',
        'form': form
    }
    return render(request, 'adminapp/admin-categories-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_category_update(request, id):
    category_select = ProductCategories.objects.get(id=id)
    if request.method == "POST":
        form = AdminCategoryUpdate(data=request.POST, instance=category_select)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_categories'))
    else:
        form = AdminCategoryUpdate(instance=category_select)

    context = {
        'title': 'Админка | Обновление категории',
        'form': form,
        'category_select': category_select
    }
    return render(request, 'adminapp/admin-categories-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_category_delete(request, id):
    ProductCategories.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('adminapp:admin_categories'))


@user_passes_test(lambda u: u.is_superuser)
def admin_products(request):
    context = {
        'title': 'Админка | Товары',
        'products': Product.objects.all()
    }
    return render(request, 'adminapp/admin-products-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_product_add(request):
    if request.method == 'POST':
        form = AdminProductAdd(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Товар успешно добавлен')
            return HttpResponseRedirect(reverse('adminapp:admin_products'))
        else:
            messages.error(request, form.errors)
            print(form.errors)
    else:
        form = AdminProductAdd()
    context = {
        'title': 'Админка | Создание товара',
        'form': form
    }
    return render(request, 'adminapp/admin-products-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_product_update(request, id):
    product_select = Product.objects.get(id=id)
    if request.method == "POST":
        form = AdminProductUpdate(data=request.POST, instance=product_select, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_products'))
    else:
        form = AdminProductUpdate(instance=product_select)

    context = {
        'title': 'Админка | Обновление информации о товаре',
        'form': form,
        'product_select': product_select
    }
    return render(request, 'adminapp/admin-products-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_product_delete(request, id):
    Product.objects.get(id=id).delete()

    return HttpResponseRedirect(reverse('adminapp:admin_products'))