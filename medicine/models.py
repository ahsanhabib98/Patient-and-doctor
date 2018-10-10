from django.db import models
from disease.models import Symptoms
from django.utils.text import slugify

# Create your models here.

class MedicineCategory(models.Model):
	name 			= models.CharField(max_length=100)

	def __str__(self):
		return self.name


class MedicineSubCategory(models.Model):
	name 			= models.CharField(max_length=100)
	details			= models.TextField()
	category 		= models.ForeignKey(MedicineCategory, on_delete=models.CASCADE, related_name='medicinecategory')

	def __str__(self):
		return self.name


class Medicinary(models.Model):
	name 			= models.CharField(max_length=100)
	details			= models.TextField()
	subcategory		= models.ForeignKey(MedicineSubCategory, on_delete=models.CASCADE, related_name='medicines')
	symptoms		= models.ManyToManyField(Symptoms, related_name='medicines')

	def __str__(self):
		return self.name

class MedicineWiseSymptom(models.Model):
	name 			= models.CharField(max_length=100)
	slug            = models.SlugField(null=True, blank=True)
	details 		= models.TextField()
	medicine 		= models.ForeignKey(Medicinary, on_delete=models.CASCADE, related_name='symptom')

	def save(self, *args, **kwargs):
		if not self.slug and self.name:
			self.slug = slugify(self.name)
		super(MedicineWiseSymptom, self).save(*args, **kwargs)

	def __str__(self):
		return self.name + ' - ' + self.medicine.name
