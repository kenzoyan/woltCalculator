
from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CartSerializer

from .delivery_fee import delivery_fee_calculator

class CartViews(APIView):
    def post(self, request):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            # serializer.save()
            cart_data = serializer.data
            deliverey_fees = delivery_fee_calculator(cart_data['cart_value'], cart_data['delivery_distance'],
                                           cart_data['number_of_items'], cart_data['time'])

            return Response({"status": "success", "deliverey_fees": deliverey_fees}, status=status.HTTP_200_OK)

        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)