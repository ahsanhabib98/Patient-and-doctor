from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('check/', check, name = 'check'),
    path('signup/', sign_up, name = 'signup'),
    path('login/', auth_views.login, {'template_name': 'userinfo/login.html'}, name = 'login'),
    path('logout/', auth_views.logout, {'template_name': 'home.html'}, name = 'logout'),
    path('profile/', profile, name = 'profile'),
    path('patient-profile/', patients_profile, name = 'patient-profile'),
    path('doctor-profile/', doctor_profile, name = 'doctor-profile'),
    path('patient-create/', patient_create, name = 'patient-create'),
    path('doctor-create/', doctor_create, name = 'doctor-create'),
    path('patient-detail/', patient_detail, name = 'patient-detail'),
    path('doctor-detail/', doctor_detail, name = 'doctor-detail'),
    path('patient-edit/', patient_edit, name = 'patient-edit'),
    path('doctor-edit/', doctor_edit, name = 'doctor-edit'),
    path('present-mode/', presentmode, name = 'present-mode'),
    path('patients/', patients, name = 'patients'),
    path('public-patient-detail/<int:id>/', public_patient_detail, name = 'public-patient'),
    path('public-doctor-detail/<int:id>/', public_doctor_detail, name = 'public-doctor'),
    path('research/', research, name = 'research'),
]
