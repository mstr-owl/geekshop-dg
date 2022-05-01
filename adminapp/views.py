from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm, AdminCategoryAdd, AdminCategoryUpdate, \
    AdminProductAdd, AdminProductUpdate
from authapp.models import User
from django.contrib.auth.decorators import user_passes_test

from adminapp.mixin import CustomDispatchMixin, BaseClassContextMixin, UserDispatchMixin
from mainapp.models import ProductCategories, Product
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView


# @user_passes_test(lambda u: u.is_superuser)
# def index(request):
#     return render(request, 'adminapp/admin.html')

class IndexTemplateView(TemplateView, BaseClassContextMixin, CustomDispatchMixin):
    template_name = 'adminapp/admin.html'
    title = 'Главня страница'

class UserListView(ListView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-read.html'
    title = 'Админка | Пользователи'
    context_object_name = 'users'

class UserCreateView(CreateView, BaseClassContextMixin, CustomDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-create.html'
    form_class = UserAdminRegisterForm
    title = 'Админка | Регистрация'
    success_url = reverse_lazy('adminapp:admin_users')

class UserUpdateView(UpdateView,BaseClassContextMixin,CustomDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    title ='Админка | Обновление пользователя'
    success_url = reverse_lazy('adminapp:admin_users')

class UserDeleteView(DeleteView,CustomDispatchMixin):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('adminapp:admin_users')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

# @user_passes_test(lambda u: u.is_superuser)
# def admin_users(request):
#     context = {
#         'title': 'Админка | Пользователи',
#         'users': User.objects.all()
#     }
#     return render(request, 'adminapp/admin-users-read.html', context)
#
# @user_passes_test(lambda u: u.is_superuser)
# def admin_user_create(request):
#     if request.method == 'POST':
#         form = UserAdminRegisterForm(data=request.POST,files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('adminapp:admin_users'))
#         else:
#             print(form.errors)
#     else:
#         form=UserAdminRegisterForm()
#         context = {
#             'title': 'Админка | Регистрация',
#             'form': form
#         }
#
#     return render(request, 'adminapp/admin-users-create.html', context)


# @user_passes_test(lambda u: u.is_superuser)
# def admin_user_update(request, id):
#     user_select = User.objects.get(id=id)
#     if request.method == 'POST':
#         form = UserAdminProfileForm(data=request.POST, instance=user_select, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('adminapp:admin_users'))
#     else:
#         form = UserAdminProfileForm(instance=user_select)
#     context = {
#          'title': 'Админка | Обновление пользователя',
#          'form': form,
#          'user_select': user_select
#     }
#     return render(request, 'adminapp/admin-users-update-delete.html', context)
#
# @user_passes_test(lambda u: u.is_superuser)
# def admin_user_delete(request, id):
#     user = User.objects.get(id=id)
#     user.is_active = False
#     user.save()
#     return HttpResponseRedirect(reverse('adminapp:admin_users'))

class CategoryListView(ListView, BaseClassContextMixin, CustomDispatchMixin, UserDispatchMixin):
    model = ProductCategories
    title = 'Админка | Категории товаров',
    template_name = 'adminapp/admin-categories-read.html'
    context_object_name = 'categories'


class CategoryCreateView(CreateView, BaseClassContextMixin, CustomDispatchMixin, UserDispatchMixin):
    model = ProductCategories
    title = 'Админка | Добавить категорию товаров'
    template_name = 'adminapp/admin-categories-create.html'
    form_class = AdminCategoryAdd
    success_url = reverse_lazy('adminapp:admin_categories')

    def form_valid(self, form):
        messages.success(self.request, f'Категория {form.clean()["name"]} успешно добавлена')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super().form_invalid(form)


class CategoryUpdateView(UpdateView, BaseClassContextMixin, CustomDispatchMixin, UserDispatchMixin):
    model = ProductCategories
    title = 'Админка | Редактировать категорию товаров'
    template_name = 'adminapp/admin-categories-update-delete.html'
    form_class = AdminCategoryUpdate
    success_url = reverse_lazy('adminapp:admin_categories')

    def form_valid(self, form):
        messages.success(self.request, f'Изменения в категорию {form.clean()["name"]} успешно внесены')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super().form_invalid(form)


class CategoryDeleteView(DeleteView, CustomDispatchMixin, UserDispatchMixin):
    model = ProductCategories
    template_name = 'adminapp/admin-categories-update-delete.html'
    form_class = AdminCategoryUpdate
    success_url = reverse_lazy('adminapp:admin_categories')

    def get(self, request, *args, **kwargs):
        pass
        self.object = self.get_object()
        obj_name = self.object.name
        self.object.delete()
        messages.success(self.request, f'Категория {obj_name} успешно удалена')
        return HttpResponseRedirect(self.success_url)

# @user_passes_test(lambda u: u.is_superuser)
# def admin_categories(request):
#     context = {
#         'title': 'Админка | Пользователи',
#         'categories': ProductCategories.objects.all()
#     }
#     return render(request, 'adminapp/admin-categories-read.html', context)
#
#
# @user_passes_test(lambda u: u.is_superuser)
# def admin_category_add(request):
#     if request.method == 'POST':
#         form = AdminCategoryAdd(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Категория успешно добавлена')
#             return HttpResponseRedirect(reverse('adminapp:admin_categories'))
#         else:
#             messages.error(request, form.errors)
#             print(form.errors)
#     else:
#         form = AdminCategoryAdd
#     context = {
#         'title': 'Админка | Добавить категорию',
#         'form': form
#     }
#     return render(request, 'adminapp/admin-categories-create.html', context)
#
#
# @user_passes_test(lambda u: u.is_superuser)
# def admin_category_update(request, id):
#     category_select = ProductCategories.objects.get(id=id)
#     if request.method == "POST":
#         form = AdminCategoryUpdate(data=request.POST, instance=category_select)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('adminapp:admin_categories'))
#     else:
#         form = AdminCategoryUpdate(instance=category_select)
#
#     context = {
#         'title': 'Админка | Обновление категории',
#         'form': form,
#         'category_select': category_select
#     }
#     return render(request, 'adminapp/admin-categories-update-delete.html', context)
#
#
# @user_passes_test(lambda u: u.is_superuser)
# def admin_category_delete(request, id):
#     ProductCategories.objects.get(id=id).delete()
#     return HttpResponseRedirect(reverse('adminapp:admin_categories'))

class ProductListView(ListView, BaseClassContextMixin, CustomDispatchMixin, UserDispatchMixin):
    model = Product
    template_name = 'adminapp/admin-products-read.html'
    title = 'Админка | Категории товаров',
    context_object_name = 'products'


class ProductCreateView(CreateView, BaseClassContextMixin, CustomDispatchMixin, UserDispatchMixin):
    model = Product
    template_name = 'adminapp/admin-products-create.html'
    title = 'Админка | Добавление товара'
    success_url = reverse_lazy('adminapp:admin_products')
    form_class = AdminProductAdd

    def form_valid(self, form):
        messages.success(self.request, f'Товар {form.clean()["name"]} успешно добавлен')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super().form_invalid(form)


class ProductUpdateView(UpdateView, BaseClassContextMixin, CustomDispatchMixin, UserDispatchMixin):
    model = Product
    template_name = 'adminapp/admin-products-update-delete.html'
    title = 'Админка | Обновление информации о товаре'
    form_class = AdminProductUpdate
    success_url = reverse_lazy('adminapp:admin_products')

    def form_valid(self, form):
        messages.success(self.request, f'Товар {form.clean()["name"]} успешно обновлен')
        return super(ProductUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return super(ProductUpdateView, self).form_invalid(form)


class ProductDeleteView(DeleteView, CustomDispatchMixin, UserDispatchMixin):
    model = Product
    template_name = 'adminapp/admin-products-update-delete.html'
    form_class = AdminProductUpdate
    success_url = reverse_lazy('adminapp:admin_products')

    def get(self, request, *args, **kwargs):
        pass
        self.object = self.get_object()
        obj_name = self.object.name
        self.object.delete()
        messages.success(self.request, f'Товар {obj_name} успешно удален')
        return HttpResponseRedirect(self.success_url)


# @user_passes_test(lambda u: u.is_superuser)
# def admin_products(request):
#     context = {
#         'title': 'Админка | Товары',
#         'products': Product.objects.all()
#     }
#     return render(request, 'adminapp/admin-products-read.html', context)
#
#
# @user_passes_test(lambda u: u.is_superuser)
# def admin_product_add(request):
#     if request.method == 'POST':
#         form = AdminProductAdd(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Товар успешно добавлен')
#             return HttpResponseRedirect(reverse('adminapp:admin_products'))
#         else:
#             messages.error(request, form.errors)
#             print(form.errors)
#     else:
#         form = AdminProductAdd()
#     context = {
#         'title': 'Админка | Создание товара',
#         'form': form
#     }
#     return render(request, 'adminapp/admin-products-create.html', context)
#
#
# @user_passes_test(lambda u: u.is_superuser)
# def admin_product_update(request, id):
#     product_select = Product.objects.get(id=id)
#     if request.method == "POST":
#         form = AdminProductUpdate(data=request.POST, instance=product_select, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('adminapp:admin_products'))
#     else:
#         form = AdminProductUpdate(instance=product_select)
#
#     context = {
#         'title': 'Админка | Обновление информации о товаре',
#         'form': form,
#         'product_select': product_select
#     }
#     return render(request, 'adminapp/admin-products-update-delete.html', context)
#
#
# @user_passes_test(lambda u: u.is_superuser)
# def admin_product_delete(request, id):
#     Product.objects.get(id=id).delete()
#
#     return HttpResponseRedirect(reverse('adminapp:admin_products'))