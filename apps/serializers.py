from rest_framework import serializers
from apps.models import  Address, Patient, Advocate, Appointment

class AddressSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Address
		fields = ('id', 'address1', 'address2', 'city','state','zip_code')

class PatientSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Patient
		fields = ('id', 'firstName', 'lastName','address','phone','uber_token')


class AdvocateSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Advocate
		fields = ('id', 'firstName', 'lastName','address','phone','uber_token','patient')

class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Appointment
		fields = ('id', 'title','address', 'description','date')

