"""acfun_front URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from ssh_qa.views import *
from api.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name="index"),
    url(r'^req/$', req, name="req"),
    url(r'^ssh_qa/$', ssh_qa, name="ssh_qa"),
    url(r'^ssh_qa_runshell/$', ssh_qa_runshell, name="ssh_qa_runshell"),
    url(r'^ssh_qa_logs/$', ssh_qa_logs, name="ssh_qa_logs"),
    url(r'^ssh_info/$', ssh_info, name="ssh_info"),
    url(r'^api/$', api, name="api"),
    ]