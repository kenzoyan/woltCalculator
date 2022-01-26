
from rest_framework import serializers

from .models import Cart

class CartSerializer(serializers.ModelSerializer):

    cart_value = serializers.IntegerField()
    delivery_distance = serializers.IntegerField()
    number_of_items = serializers.IntegerField()
    time = serializers.DateTimeField()

    class Meta:
        model = Cart
        fields = ('__all__')