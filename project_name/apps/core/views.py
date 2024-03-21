# from django.shortcuts import render
# from django.shortcuts import redirect
from django.http import HttpResponse


# Create your views here.
# def redirect_admin(request):
#     return redirect('/admin/')


def core_urls_views(request):
    response = "This is core/ urls!"
    return HttpResponse(response)
