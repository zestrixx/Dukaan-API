from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from .models import OrderDetails, Orders, CustomerDetails

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'

class OrderDetailsSerializer(serializers.ModelSerializer):
    orders = OrdersSerializer()
    class Meta:
        model = OrderDetails
        fields = '__all__'

    def create(self, validated_data):
        return super().create(validated_data)
