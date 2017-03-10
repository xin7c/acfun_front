from django.shortcuts import render
from django.http import HttpResponse
from .models import API_VERSION

def api(req):
    if req.method == "GET":
        addr = req.META['REMOTE_ADDR']
        apis = API_VERSION.objects.all()
        context = {}
        context['addr'] = addr
        context['apis'] = apis
        response = render(req, 'api.html', context=context)
        response["hd"] = "1024"
        response.set_cookie(key="cookie_api", value="2017")
        # print req.META['HTTP_USER_AGENT']
        return response


def api_r(req):
    if req.method == "POST":
        choice_api = req.POST["choice_api"]
        return HttpResponse(choice_api)


def login(req):
    return HttpResponse("Login")


def logout(req):
    return HttpResponse("Logout")
