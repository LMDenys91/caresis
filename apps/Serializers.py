from rest_framework import serializers
from apps.models import  Address, Patient, Advocate, Appointment, Status_Update

class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ('id', 'address1', 'address2', 'city','state','zip_code')

class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ('id', 'firstName', 'lastName', 'address','phone','uber_token')


class AdvocateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Advocate
        fields = ('id', 'firstName', 'lastName', 'address','phone','uber_token','patient')

class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appointment
        fields = ('id', 'advocate', 'title', 'description','address','date')

class Status_UpdateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Status_Update
        fields = ('id', 'appointment', 'time', 'question')