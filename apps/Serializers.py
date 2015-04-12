from rest_framework import serializers
from apps.models import  Address, Patient, Advocate, Appointment, Status_Update

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')