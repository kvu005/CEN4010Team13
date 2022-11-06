from rest_framework import serializers
from cards.models import CreditCard


class BaseCreditCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields = '__all__'
