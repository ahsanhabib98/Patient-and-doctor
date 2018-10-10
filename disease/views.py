from django.shortcuts import render
from .models import*
from medicine.models import*
from .models import*
from userinfo.models import Patient

# Create your views here.

def disease_category(request):
	category = DiseaseCategory.objects.all()
	query = request.GET.get('q', None)
	if query:
		category = category.filter(
				Q(name__incontains=query)
			)
	context = {'category': category}
	template = 'disease/category.html'
	return render(request, template, context)

def diseasewise_symptoms(request, id):
	disease = Diseases.objects.get(id = id)
	patients = Patient.objects.filter(prescription__icontains = disease.name)
	patients_num = len(patients)
	symptoms = disease.symptoms.all()
	context = {
		'disease': disease,
		'patients_num': patients_num,
		'symptoms': symptoms,
		}

	template = 'disease/diseasewise-symptoms.html'
	return render(request, template, context)

def symptoms(request):
	symptoms = SubSymptoms.objects.all()
	context = {
		'symptoms': symptoms,
	}
	template = 'disease/symptoms.html'
	return render(request, template, context)

def symptomswise(request, slug):
	symptoms = Symptoms.objects.filter(slug=slug)
	symptom = symptoms[0:1]
	context = {
		'slug': slug,
		'symptoms': symptoms,
		'symptom': symptom,
	}
	template = 'disease/symptomswise.html'
	return render(request, template, context)

def symptom_detail(request, slug):
	symptom = SubSymptoms.objects.get(slug=slug)
	context = {
		'symptom': symptom,
	}
	template = 'disease/symptom-detail.html'
	return render(request, template, context)
