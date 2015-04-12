import json

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
# Create your views here.

@api_view(['GET', 'POST'])
def appointment(request):
	return Response(status=status.HTTP_201_CREATED)

		
