from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, Select, Textarea
from .models import *

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields=['username','password1','password2']
        widgets = {
            'username': TextInput(attrs={'class':'form-control'}),
        }

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        exclude = ['user', ]

        widgets = {
            'profile_name': TextInput(attrs={'class':'form-control'}),
            'title': Select(attrs={'class':'form-control'}),
            'gender': Select(attrs={'class':'form-control'}),
            'division': Select(attrs={'class':'form-control'}),
            'district': Select(attrs={'class':'form-control'}),
            'birth_day': TextInput(attrs={'class':'form-control'}),
            'phone': TextInput(attrs={'class':'form-control'}),
            'prescription': Textarea(attrs={'class':'form-control'}),
            'interest': Textarea(attrs={'class':'form-control'}),
        }

class PresentModeForm(forms.ModelForm):
    class Meta:
        model = PresentPosition
        fields = '__all__'
        exclude = ['patient', ]

        widgets = {
            'details': Textarea(attrs={'class':'form-control'}),
            'symptoms': Select(attrs={'class':'form-control'}),
            'medicine': Select(attrs={'class':'form-control'}),
            'disease': Select(attrs={'class':'form-control'}),
        }


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'
        exclude = ['user', ]

        widgets = {
            'profile_name': TextInput(attrs={'class':'form-control'}),
            'title': Select(attrs={'class':'form-control'}),
            'gender': Select(attrs={'class':'form-control'}),
            'division': Select(attrs={'class':'form-control'}),
            'district': Select(attrs={'class':'form-control'}),
            'birth_day': TextInput(attrs={'class':'form-control'}),
            'phone': TextInput(attrs={'class':'form-control'}),
            'qualification': Textarea(attrs={'class':'form-control'}),
            'interest': Textarea(attrs={'class':'form-control'}),
        }

class ResearchForm(forms.ModelForm):
    class Meta:
        model = Research
        fields = '__all__'
        exclude = ['profile', ]

        widgets = {
            'details': Textarea(attrs={'class':'form-control'}),
        }
