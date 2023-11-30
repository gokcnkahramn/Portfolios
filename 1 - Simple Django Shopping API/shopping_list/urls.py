from django.urls import path
from .views import ShoppingListView

urlpatterns = [
    path('api/shopping-list/', ShoppingListView.as_view(), name='shopping-list'),
]
