from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from .models import NoteModel
from .serializers import NoteModelSerializer

class NoteListCreateAPIView(ListCreateAPIView):
    queryset = NoteModel.objects.all()
    serializer_class = NoteModelSerializer

class NoteRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = NoteModel.objects.all()
    serializer_class = NoteModelSerializer