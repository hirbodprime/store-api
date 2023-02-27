from rest_framework import serializers
from .models import InvoiceModel

class InvoiceModelSerializer(serializers.ModelSerializer):
    # status = serializers.BooleanField(read_only=True)
    class Meta:
        model = InvoiceModel
        fields = '__all__'