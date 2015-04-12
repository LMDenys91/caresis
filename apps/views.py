import json
import requests
from django.http import HttpResponse
from twilio.rest import TwilioRestClient
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext, loader , Context
from django.shortcuts import redirect ,render_to_response

from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView

from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route

from apps.models import Appointment, Advocate, Appointment, Patient, Address
from apps.erializers import AppointmentSerializer, AdvocateSerializer, AppointmentSerializer, PatientSerializer, AddressSerializer

# Create your views here.

@api_view(['GET', 'POST'])

def appointment(request):
	if request.method == 'GET':
		queryset = Appointment.objects.all()
		serializer = AppointmentSerializer(queryset, many=True)
		return Response(serializer.data)
	return Response(status=status.HTTP_201_CREATED)
    if request.method == 'POST':
        ap =  Appointment(
		 	title = request.DATA.get("title"),
		 	description = request.DATA.get("description"),
		 	date = request.DATA.get("date"),
			address = request.DATA.get("address")
            )

        ap.save()
        return Response(status=status.HTTP_201_CREATED)

def advocate(request):
	if request.method == 'GET':
		queryset = Advocate.objects.all()
		serializer = AdvocateSerializer(queryset, many=True)
		return Response(serializer.data)
	return Response(status=status.HTTP_201_CREATED)

def address(request):
	if request.method == 'GET':
		queryset = Address.objects.all()
		serializer = AddressSerializer(queryset, many=True)
		return Response(serializer.data)
	return Response(status=status.HTTP_201_CREATED)

def patient(request):
	if request.method == 'GET':
		queryset = Patient.objects.all()
		serializer = PatientSerializer(queryset, many=True)
		return Response(serializer.data)
	return Response(status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def sms(request):
	account_sid = "AC3a1890bb443c5abe1a07624e0c5624b2"
	auth_token  = "59da12d6e084150099a80e398acc29a3"
	client = TwilioRestClient(account_sid, auth_token)
	 
	message = client.messages.create(body="Jenny please?! I love you <3",
	    to="+15519987206",    # Replace with your phone number
	    from_="+16462333216") # Replace with your Twilio number
	#print message.sid
	return HttpResponse(status=201)


@api_view(['GET', 'POST'])
def uber_callback(request):
	parameters = {
		'redirect_uri': 'INSERT_ROUTE_TO_STEP_TWO',
	    	'code': request.GET.get('code', ''),
	    	# 'code': 'El34AvVt6Ismf688HJZ0ascNGXAWoI',
		'grant_type': 'authorization_code',
	}

	response = requests.post('https://login.uber.com/oauth/token',auth=('oQ3VN3DLkVAETHYFwPLnw0JbgHwwxzro','FXt5qBewJCzYC642XVa0APR6NoShI0ahlB3QyTcD',),data=parameters,)
	print request.GET.get('code', '')
	print response
	access_token = response.json().get('access_token')
	return HttpResponse(access_token, content_type="application/json")
	#return HttpResponse(status=404)
