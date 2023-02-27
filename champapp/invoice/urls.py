from django.urls import path
from .views import InvoiceListCreateAPIView , InvoiceRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('list-create/',InvoiceListCreateAPIView.as_view()),
    path('get-update-destroy/<int:pk>',InvoiceRetrieveUpdateDestroyAPIView.as_view())
]