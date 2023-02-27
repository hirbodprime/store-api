from django.contrib import admin
from .models import ProductModel

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id' , 'code' , 'title']
    fieldsets = [
        ('Product Data', {'fields':['title' , 'image','description','location','quantity' ,'producttype']}),
    ]
admin.site.register(ProductModel , ProductAdmin)