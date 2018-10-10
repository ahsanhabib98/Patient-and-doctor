from django.urls import path
from .views import *


urlpatterns = [
    path('disease-category/', disease_category, name = 'disease-category'),
    path('diseasewise-symptoms/<int:id>/', diseasewise_symptoms, name = 'diseasewise-symptoms'),
    path('symptoms/', symptoms, name = 'symptoms'),
    path('symptomswise/<slug:slug>/', symptomswise, name = 'symptomswise'),
    path('symptom-detail/<slug:slug>/', symptom_detail, name = 'symptom-detail'),
]
