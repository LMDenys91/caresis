from django.conf.urls import patterns, url , include
from rest_framework import routers
from apps import views


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^caresis/', api.caresis, name='caresis'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
