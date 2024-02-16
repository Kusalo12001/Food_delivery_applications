
# pricing/urls.py
from django.urls import path
from .views import CalculatePrice

urlpatterns = [
    path('calculate-price/', CalculatePrice.as_view(), name='calculate_price'),
]
