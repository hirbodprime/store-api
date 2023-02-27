from rest_framework import serializers
from .models import ProductModel

class ProductModelSerializer(serializers.ModelSerializer):
    Done = serializers.BooleanField(read_only=True)
    class Meta:
        model = ProductModel
        fields = '__all__'