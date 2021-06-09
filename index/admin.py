from django.contrib import admin

# Register your models here.
from .Models.models import Product
from .Models.category import Category
from .Models.smartfarming import smartfar
from .Models.order import Order
class AdminProduct(admin.ModelAdmin):
    list_display=['productname','category']

class AdminCategory(admin.ModelAdmin):
    list_display=['name']

admin.site.register(Product, AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(smartfar)
admin.site.register(Order)
