from django.urls import path
from .views import app1_urls

urlpatterns = [   
    path('', app1_urls, name='app1_urls'), 
]