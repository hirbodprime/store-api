from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from .models import InvoiceModel
from .serializers import InvoiceModelSerializer

class InvoiceListCreateAPIView(ListCreateAPIView):
    queryset = InvoiceModel.objects.all()
    serializer_class = InvoiceModelSerializer

class InvoiceRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = InvoiceModel.objects.all()
    serializer_class = InvoiceModelSerializer