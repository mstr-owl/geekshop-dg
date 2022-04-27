from django.contrib import admin

from authapp.models import User

# admin.site.register(User)
from basket.admin import BasketAdmin
from basket.models import Basket

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = Basket
    inlines = (BasketAdmin,)