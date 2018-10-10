from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from medicine.models import Medicinary
from disease.models import Symptoms, Diseases

# Create your models here.

class Division(models.Model):
    division_name           =        models.CharField(max_length=50)
    def __str__(self):
        return self.division_name

class District(models.Model):
    district_name           =        models.CharField(max_length=50)
    division                =        models.ForeignKey(Division, on_delete=models.CASCADE)
    def __str__(self):
        return self.district_name

class Patient(models.Model):
    title_choice = (
        ('Mr.', 'Mr'),
        ('Miss', 'Miss'),
        ('Ms.', 'Ms.'),
        ('Mrs.', 'Mrs'),
        ('Ir.', 'Ir'),
        ('Dr.', 'Dr'),
        ('Drs', 'Drs'),
        ('Professor', 'Professor'),
    )
    gender_choice = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    user                    =        models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image           =        models.ImageField(upload_to='patient_image', blank=True)
    profile_name            =        models.CharField(unique=True, max_length=50)
    title                   =        models.CharField(max_length=20, choices=title_choice)
    gender                  =        models.CharField(max_length=10, choices=gender_choice)
    division                =        models.ForeignKey(Division, on_delete=models.CASCADE)
    district                =        models.ForeignKey(District, on_delete=models.CASCADE)
    birth_day               =        models.DateField()
    phone                   =        models.IntegerField()
    prescription           	=        models.TextField()
    interest             	=        models.TextField()
    created                 =        models.DateField(auto_now_add=True)
    updated                 =        models.DateField(auto_now=True)

    def __str__(self):
        return self.profile_name

    class Meta:
        ordering = ["-id"]

class PresentPosition(models.Model):
    details                 =        models.TextField()
    patient                 =        models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='modes')
    symptoms                =        models.ForeignKey(Symptoms, on_delete=models.CASCADE, related_name='modes')
    medicine                =        models.ForeignKey(Medicinary, on_delete=models.CASCADE, related_name='modes')
    disease                 =        models.ForeignKey(Diseases, on_delete=models.CASCADE, related_name='modes')

    def __str__(self):
        return self.patient.profile_name

    class Meta:
        ordering = ["-id"]

class Doctor(models.Model):
    title_choice = (
        ('Mr.', 'Mr'),
        ('Miss', 'Miss'),
        ('Ms.', 'Ms.'),
        ('Mrs.', 'Mrs'),
        ('Ir.', 'Ir'),
        ('Dr.', 'Dr'),
        ('Drs', 'Drs'),
        ('Professor', 'Professor'),
    )
    gender_choice = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    user                    =        models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image           =        models.ImageField(upload_to='doctor_image', blank=True)
    profile_name            =        models.CharField(unique=True, max_length=50)
    title                   =        models.CharField(max_length=20, choices=title_choice)
    gender                  =        models.CharField(max_length=10, choices=gender_choice)
    division                =        models.ForeignKey(Division, on_delete=models.CASCADE)
    district                =        models.ForeignKey(District, on_delete=models.CASCADE)
    birth_day               =        models.DateField()
    phone                   =        models.IntegerField()
    qualification           =        models.TextField()
    interest                =        models.TextField()
    created                 =        models.DateField(auto_now_add=True)
    updated                 =        models.DateField(auto_now=True)

    def __str__(self):
        return self.profile_name

    class Meta:
        ordering = ["-id"]


class Research(models.Model):
    profile                 =  models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='research')
    research_image          =  models.ImageField(upload_to='research_image', blank=True)
    details                 =  models.TextField()


    def __str__(self):
        return self.profile.profile_name
