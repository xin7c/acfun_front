#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from .models import API_VERSION
from django.forms.models import model_to_dict
# from django.core import serializers
# import json

def api(req):
    if req.method == "GET":
        addr = req.META['REMOTE_ADDR']
        HTTP_USER_AGENT = req.META['HTTP_USER_AGENT']
        # get mysql
        apis = API_VERSION.objects.values()
        apis_list = [x["api_version"] for x in apis]
        last_version = max(apis_list)
        context = {}
        context['addr'] = addr
        context['apis'] = apis
        context['apis_list'] = apis_list
        context['last_version'] = last_version
        context['HTTP_USER_AGENT'] = HTTP_USER_AGENT
        response = render(req, 'api.html', context=context)
        response["hd"] = "1024"
        response.set_cookie(key="cookie_api", value="2017")
        # print req.META
        return response


def api_r(req):
    if req.method == "POST":
        choice_api = req.POST["choice_api"]
        print API_VERSION.objects.all()
        r_api_version = API_VERSION.objects.get(api_version__exact="1.0.2")

        # 第一种方法: serializers + json
        # print json.loads(serializers.serialize("json", r_api_version))[0]["fields"]["api_version"]

        # 第二种方法: model_to_dict
        data = model_to_dict(r_api_version)["api_version"]
        if data == choice_api:
            return HttpResponse("[CheckSuccsess]" + choice_api)
        else:
            return HttpResponse("[NotMatch]" + choice_api)



def login(req):
    return HttpResponse("Login")


def logout(req):
    return HttpResponse("Logout")
