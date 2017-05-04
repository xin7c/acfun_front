from django.shortcuts import render

# Create your views here.
def vueJS_index(req):
    return render(req, "vueJS_index.html", context={})