from django.contrib import admin
from .models import InvoiceModel

class InvoiceModelAdmin(admin.ModelAdmin):
    list_display = ['id' , 'productlist' , 'status','invoicenumber']
    fieldsets = [
        ('Product Data', {'fields':['productlist' , 'status','invoicenumber']}),
    ]
admin.site.register(InvoiceModel , InvoiceModelAdmin)