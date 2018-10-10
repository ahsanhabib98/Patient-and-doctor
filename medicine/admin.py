from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(MedicineCategory)
admin.site.register(MedicineSubCategory)
admin.site.register(Medicinary)
admin.site.register(MedicineWiseSymptom)