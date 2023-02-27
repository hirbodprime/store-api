from django.urls import path
from .views import ProductListCreateAPIView , ProductRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('list-create/',ProductListCreateAPIView.as_view()),
    path('get-update-destroy/<int:pk>',ProductRetrieveUpdateDestroyAPIView.as_view())
]