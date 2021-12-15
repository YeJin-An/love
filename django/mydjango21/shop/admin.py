from django.contrib import admin
from shop.models import Category, Shop, Tag 
from shop.forms import ShopForm


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    form = ShopForm

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
