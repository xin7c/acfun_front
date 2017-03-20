from django.shortcuts import render

# Create your views here.
def ajs_index(req):
    return render(req, "ajs_index.html", context={})
