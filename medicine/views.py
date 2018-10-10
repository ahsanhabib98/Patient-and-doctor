from django.shortcuts import render
from .models import *
from userinfo.models import Patient

# Create your views here.

def medicine_category(request):
	category = MedicineCategory.objects.all()
	context = {'category': category}
	template = 'medicine/category.html'
	return render(request, template, context)

def subwise_medicine(request, id):
	subcategory = MedicineSubCategory.objects.get(id=id)
	patients = Patient.objects.filter(prescription__icontains = subcategory.name)
	patients_num = len(patients)
	context = {
		'subcategory': subcategory,
		'patients_num': patients_num,
		}
	template = 'medicine/sub-category.html'
	return render(request, template, context)

def medicinewise_symptom(request, id):
	medicine = Medicinary.objects.get(id=id)
	patients = Patient.objects.filter(prescription__icontains = medicine.name)
	patients_num = len(patients)
	symptoms = MedicineWiseSymptom.objects.filter(medicine__id=id)
	context = {
		'medicine': medicine,
		'patients_num': patients_num,
		'symptoms': symptoms,
	}
	template = 'medicine/medicinewise.html'
	return render(request, template, context)
