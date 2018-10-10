from django.db import models
from django.utils.text import slugify

# Create your models here.

class DiseaseCategory(models.Model):
	name 			= models.CharField(max_length=100)

	def __str__(self):
		return self.name


class Diseases(models.Model):
	name 			= models.CharField(max_length=100)
	details			= models.TextField()
	category 		= models.ForeignKey(DiseaseCategory, on_delete=models.CASCADE, related_name='disease')

	def __str__(self):
		return self.name


class Symptoms(models.Model):
	name 			= models.CharField(max_length=100)
	slug            = models.SlugField(null=True, blank=True)
	details			= models.TextField()
	disease  		= models.ForeignKey(Diseases, on_delete=models.CASCADE, related_name='symptoms')

	def save(self, *args, **kwargs):
		if not self.slug and self.name:
			self.slug = slugify(self.name)
		super(Symptoms, self).save(*args, **kwargs)

	def __str__(self):
		return self.disease.name+' - '+self.name

class SubSymptoms(models.Model):
	name = models.CharField(max_length=100)
	details = models.TextField()
	slug = models.SlugField(null=True, blank=True)

	def save(self, *args, **kwargs):
		if not self.slug and self.name:
			self.slug = slugify(self.name)
		super(SubSymptoms, self).save(*args, **kwargs)

	def __str__(self):
		return self.name
