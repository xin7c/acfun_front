from django.shortcuts import render
from django.http import HttpResponse

def api(req):
    context = {}
    response = render(req, 'api.html',context=context)
    response["hd"] = "1024"
    response.set_cookie(key="cookie_api", value="2017")
    print response.has_header("hd")
    print response.cookies
    return response
