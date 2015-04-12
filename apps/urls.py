from django.conf.urls import patterns, url , include
from rest_framework import routers
from apps import views

router = routers.DefaultRouter()

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^appointment/', views.appointment, name='appointment'),
    url(r'^address/', views.address, name='address'),
    url(r'^patient/', views.patient, name='patient'),
    url(r'^advocate/', views.advocate, name='advocate'),
    url(r'^address/', views.address, name='address'),
    url(r'^sms/', views.sms, name='sms'),
    url(r'^uber_callback/', views.uber_callback, name='uber_callback')
]
