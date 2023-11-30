from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ShoppingItem
from .serializers import ShoppingItemSerializer

class ShoppingListView(APIView):
    def get(self, request):
        shopping_items = ShoppingItem.objects.all()
        serializer = ShoppingItemSerializer(shopping_items, many=True)
        return Response(serializer.data)
