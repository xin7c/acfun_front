from django.shortcuts import render
from django.http import HttpResponse


def api(req):
    addr = req.META['REMOTE_ADDR']
    context = {}
    context['addr'] = addr
    response = render(req, 'api.html', context=context)
    response["hd"] = "1024"
    response.set_cookie(key="cookie_api", value="2017")
    print req.META['HTTP_USER_AGENT']
    print
    return response


def login(req):
    return HttpResponse("Login")


def logout(req):
    return HttpResponse("Logout")
