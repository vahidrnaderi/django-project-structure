from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def app2_urls(request):
    response="This is app2/ urls!"
    return HttpResponse(response)
