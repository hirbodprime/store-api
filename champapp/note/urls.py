from django.urls import path
from .views import NoteListCreateAPIView , NoteRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('list-create/',NoteListCreateAPIView.as_view()),
    path('get-update-destroy/<int:pk>',NoteRetrieveUpdateDestroyAPIView.as_view())
]