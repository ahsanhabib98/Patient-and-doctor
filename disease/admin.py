from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(DiseaseCategory)
admin.site.register(Diseases)
admin.site.register(Symptoms)
admin.site.register(SubSymptoms)
