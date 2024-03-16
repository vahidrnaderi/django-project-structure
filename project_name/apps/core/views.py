# from django.shortcuts import render
from django.shortcuts import redirect


# Create your views here.
def redirect_admin(request):
    return redirect('/admin/')
