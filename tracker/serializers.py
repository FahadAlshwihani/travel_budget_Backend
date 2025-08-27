from rest_framework import serializers
from .models import Trip, Expense
import uuid  # Only if you're generating random trip codes

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'

    def create(self, validated_data):
        validated_data['code'] = uuid.uuid4().hex[:6].upper()
        return super().create(validated_data)

class ExpenseSerializer(serializers.ModelSerializer):
    trip = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Expense
        fields = ['id', 'title', 'amount', 'category', 'created_at', 'trip', 'payer']


