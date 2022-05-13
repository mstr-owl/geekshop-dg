from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from authapp.models import User
from mainapp.models import ProductCategories, Product


class UserAdminRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'last_name', 'first_name', 'email', 'image', 'age')

    def __init__(self, *args, **kwargs):
        super(UserAdminRegisterForm, self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['password1'].widget.attrs['placeholder'] = 'Введите пароль'
        self.fields['password2'].widget.attrs['placeholder'] = 'Повторите пароль'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Ведите фамилию'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Введите имя'
        self.fields['email'].widget.attrs['placeholder'] = 'Введите email'
        self.fields['image'].widget.attrs['placeholder'] = 'Добавить фотографию'
        self.fields['age'].widget.attrs['placeholder'] = 'Возраст'


        for filed_name , field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'

class UserAdminProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'last_name', 'first_name', 'email', 'image', 'age')

    def __init__(self, *args, **kwargs):
        super(UserAdminProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = True
        # self.fields['email'].widget.attrs['readonly'] = True

        for filed_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'



class AdminCategoryAdd(forms.ModelForm):
    class Meta:
        model = ProductCategories
        fields = ('name', 'descriptions')

    def __init__(self, *args, **kwargs):
        super(AdminCategoryAdd, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Введите имя категории'
        self.fields['descriptions'].widget.attrs['placeholder'] = 'Введите описание...'

        for filed_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'


class AdminCategoryUpdate(forms.ModelForm):
    class Meta:
        model = ProductCategories
        fields = ('name', 'descriptions')

    def __init__(self, *args, **kwargs):
        super(AdminCategoryUpdate, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Введите имя категории'
        self.fields['descriptions'].widget.attrs['placeholder'] = 'Введите описание...'

        for filed_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'



class AdminProductAdd(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'image', 'descriptions', 'price', 'quantity', 'category')

    def __init__(self, *args, **kwargs):
        super(AdminProductAdd, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Введите наименование товара'
        self.fields['image'].widget.attrs['placeholder'] = 'Загрузить фото'
        self.fields['descriptions'].widget.attrs['placeholder'] = 'Введите описание'
        self.fields['price'].widget.attrs['placeholder'] = 'Укажите цену'
        self.fields['quantity'].widget.attrs['placeholder'] = 'Укажите колличество на складе'
        self.fields['category'].widget.attrs['placeholder'] = 'Выбирите категорию'

        for filed_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-2'

        self.fields['image'].widget.attrs['class'] = 'custom-file-input'


class AdminProductUpdate(AdminProductAdd):
    class Meta:
        model = Product
        fields = ('name', 'image', 'descriptions', 'price', 'quantity', 'category')

    def __init__(self, *args, **kwargs):
        super(AdminProductUpdate, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Введите наименование товара'
        self.fields['image'].widget.attrs['placeholder'] = 'Загрузить фото'
        self.fields['descriptions'].widget.attrs['placeholder'] = 'Введите описание'
        self.fields['price'].widget.attrs['placeholder'] = 'Укажите цену'
        self.fields['quantity'].widget.attrs['placeholder'] = 'Укажите колличество на складе'
        self.fields['category'].widget.attrs['placeholder'] = 'Выбирите категорию'

        for filed_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-2'

        self.fields['image'].widget.attrs['class'] = 'custom-file-input'