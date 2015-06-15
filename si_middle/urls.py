"""si_middle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
import json
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.response import Response
from rest_framework.views import APIView
import urllib.request

class Forward(APIView):
    def get(self, request):
        req = "http://www.rit.edu/studentaffairs/siapp/get.php?"
        for key in request.QUERY_PARAMS:
            req += (key + '=' + request.QUERY_PARAMS[key] + '&')
        data = urllib.request.urlopen(req[:-1]).read().decode('utf-8')
        return Response(json.loads(data))


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'get.php/', Forward.as_view())
]

