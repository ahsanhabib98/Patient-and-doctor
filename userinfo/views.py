from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *

# Create your views here.

def check(request):
	template = 'check.html'
	return render(request, template)

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('check')
    else:
        form = SignUpForm()
    template = 'userinfo/signup.html'
    context = {'form':form}
    return render(request, template, context)

@login_required(login_url='login')
def patients_profile(request):
    template = 'userinfo/patients/patient-profile.html'
    return render(request, template)

@login_required(login_url='login')
def doctor_profile(request):
    template = 'userinfo/doctor/doctor-profile.html'
    return render(request, template)

@login_required(login_url='login')
def patient_create(request):
    form = PatientForm()
    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.user = request.user
            patient.save()
            return redirect('patient-detail')
    context = {'form':form}
    template = 'userinfo/patients/patient-create.html'
    return render(request, template, context)

@login_required(login_url='login')
def doctor_create(request):
    form = DoctorForm()
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES)
        if form.is_valid():
            doctor = form.save(commit=False)
            doctor.user = request.user
            doctor.save()
            return redirect('doctor-detail')
    context = {'form':form}
    template = 'userinfo/doctor/doctor-create.html'
    return render(request, template, context)

def patient_detail(request):
	try:
		patient = Patient.objects.get(user=request.user)
		context = {'patient': patient}
	except:
		context = {'errmsg': 'You have no profile'}
	template = 'userinfo/patients/patient-detail.html'
	return render(request, template, context)

def public_patient_detail(request, id):
	patient = Patient.objects.get(id=id)
	context = {'patient': patient}
	template = 'userinfo/patients/patient-detail.html'
	return render(request, template, context)

def doctor_detail(request):
	try:
		doctor = Doctor.objects.get(user=request.user)
		context = {'doctor': doctor}
	except:
		context = {'errmsg': 'You have no profile'}
	template = 'userinfo/doctor/doctor-detail.html'
	return render(request, template, context)


def public_doctor_detail(request, id):
	doctor = Doctor.objects.get(id=id)
	context = {'doctor': doctor}
	template = 'userinfo/doctor/doctor-detail.html'
	return render(request, template, context)


def profile(request):
	template = 'userinfo/profile.html'
	return render(request, template)

@login_required(login_url='login')
def patient_edit(request):
    patient = get_object_or_404(Patient, user=request.user)
    form = PatientForm(instance=patient)
    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES, instance=patient)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.user = request.user
            patient.save()
            return redirect('/userinfo/patient-detail/')
    context = {'form':form}
    template = 'userinfo/patients/patient-edit.html'
    return render(request, template, context)

@login_required(login_url='login')
def doctor_edit(request):
    doctor = get_object_or_404(Doctor, user=request.user)
    form = DoctorForm(instance=doctor)
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES, instance=doctor)
        if form.is_valid():
            doctor = form.save(commit=False)
            doctor.user = request.user
            doctor.save()
            return redirect('/userinfo/doctor-detail/')
    context = {'form':form}
    template = 'userinfo/doctor/doctor-edit.html'
    return render(request, template, context)


def presentmode(request):
	form = PresentModeForm()
	if request.method == 'POST':
		form = PresentModeForm(request.POST)
		patient = get_object_or_404(Patient, user=request.user)
		if form.is_valid():
			profiles = form.save(commit=False)
			profiles.patient = patient
			profiles.save()
			form = PresentModeForm()
			all_mode = PresentPosition.objects.all()
			context = {
				'form': form,
				'all_mode': all_mode,
			}
			template = 'userinfo/patients/present-mode.html'
			return render(request, template, context)
	all_mode = PresentPosition.objects.all()

	context = {
			'form':form,
			'all_mode': all_mode,
		}
	template = 'userinfo/patients/present-mode.html'
	return render(request, template, context)

def patients(request):
	patients = Patient.objects.all()
	context = {
		'patients': patients,
	}
	template = 'userinfo/patients/patients.html'
	return render(request, template, context)

def research(request):
	form = ResearchForm()
	if request.method == 'POST':
		form = ResearchForm(request.POST, request.FILES)
		doctor = get_object_or_404(Doctor, user=request.user)
		if form.is_valid():
			profiles = form.save(commit=False)
			profiles.profile = doctor
			profiles.save()
			form = ResearchForm()
			all_research = Research.objects.all()
			context = {
				'form': form,
				'all_research': all_research,
			}
			template = 'userinfo/doctor/research.html'
			return render(request, template, context)
	all_research = Research.objects.all()

	context = {
			'form':form,
			'all_research': all_research,
		}
	template = 'userinfo/doctor/research.html'
	return render(request, template, context)
