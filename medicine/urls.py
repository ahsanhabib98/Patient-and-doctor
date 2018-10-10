from django.urls import path
from .views import *


urlpatterns = [
    path('medicine-category/', medicine_category, name = 'medicine-category'),
    path('subwise-medicine/<int:id>/', subwise_medicine, name = 'subwise-medicine'),
    path('medicinewise-symptom/<int:id>/', medicinewise_symptom, name = 'medicinewise-symptom'),
]
