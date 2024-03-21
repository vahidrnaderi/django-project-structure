# from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def app2_urls_views(request):
    response = "This is app2/ urls!"
    return HttpResponse(response)
