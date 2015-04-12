from django.db import models
from django import forms

class Address(models.Model):
	id = models.AutoField(primary_key=True)
	address1 = models.CharField(max_length=200)
	address2 = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	state = models.CharField(max_length=200)
	zip_code = models.CharField(max_length=200)

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
	phone = forms.RegexField(regex=r'^\+?1?\d{9,15}$', 
                                error_message = ("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."))
	uber_token = models.CharField(max_length=200)
	address = models.CharField(max_length=200)

	def __str__(self):
        	return self.firstName


class Appointment(models.Model):
 	id = models.AutoField(primary_key=True)
 	title = models.CharField(max_length=200)
 	description = models.CharField(max_length=200)
 	date = models.DateTimeField('Time of appointment')
	address = models.CharField(max_length=200)

 	def __str__(self):
 		return self.title




