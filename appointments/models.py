from django.db import models

class Patient(models.Model):
	id = models.AutoField(primary_key=True)
	firstName = models.CharField(max_length=200)
	lastName = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	phone = forms.RegexField(regex=r'^\+?1?\d{9,15}$', 
                                error_message = ("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."))
	uber_token = models.CharField(max_length=200)
	primary_advocate = models.ForeignKey(Advocate)

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
	patient_list = models.ManyToManyField(Patient)

	def __str__(self):
        return self.firstName

 class Appointment(models.Model):
 	id = models.AutoField(primary_key=True)
 	patient = models.ForeignKey(Patient)
 	title = models.CharField(max_length=200)
 	description = models.CharField(max_length=200)
 	latitude = models.FloatField(max_digits=20)
 	longitude = models.FloatField(max_digits=20)
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




