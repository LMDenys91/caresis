from django.db import models
from django import forms

class Patient(models.Model):
	id = models.AutoField(primary_key=True)
	firstName = models.CharField(max_length=200)
	lastName = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	phone = forms.RegexField(regex=r'^\+?1?\d{9,15}$', 
                                error_message = ("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."))
	uber_token = models.CharField(max_length=200)

	def __str__(self):
        	return self.firstName

class Advocate(models.Model):
	id = models.AutoField(primary_key=True)
	firstName = models.CharField(max_length=200)
	lastName = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	phone = forms.RegexField(regex=r'^\+?1?\d{9,15}$', 
                                error_message = ("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."))
	uber_token = models.CharField(max_length=200)
	patient = models.ForeignKey(Patient)

	def __str__(self):
        	return self.firstName


class Appointment(models.Model):
 	id = models.AutoField(primary_key=True)
	advocate = models.ForeignKey(Advocate)
 	title = models.CharField(max_length=200)
 	description = models.CharField(max_length=200)
 	latitude = models.FloatField()
 	longitude = models.FloatField()
 	date = models.DateTimeField('Time of appointment')

 	def __str__(self):
 		return self.title


class Status_Update(models.Model):
 	id = models.AutoField(primary_key=True)
 	appointment = models.ForeignKey(Appointment)
 	time = models.DateTimeField('Time of update')
 	question = models.BooleanField()

 	def __str__(self):
 		return self.time


