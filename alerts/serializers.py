from rest_framework import serializers
from .models import Alert


class AlertSerializer(serializers.ModelSerializer):
    coin_name = serializers.CharField(read_only=True, required=False)

    class Meta:
        model = Alert
        fields = ['id', 'user', 'coin_name', 'price', 'status']
        extra_kwargs = {'user': {'required': False}}
