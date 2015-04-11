from django.conf.urls import patterns, url , include
from rest_framework import routers
from apps import views

router = routers.DefaultRouter()
router.register(r'appointment', views.appointment)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
