from rest_framework import serializers
from .models import NoteModel

class NoteModelSerializer(serializers.ModelSerializer):
    code = serializers.CharField(read_only=True)
    class Meta:
        model = NoteModel
        fields = '__all__'