from django.db import models
from product.models import ProductModel





class InvoiceModel(models.Model):
    invoicenumber = models.CharField(max_length=50)
    status = models.BooleanField(default=False)
    productlist = models.ForeignKey(ProductModel, on_delete=models.CASCADE)