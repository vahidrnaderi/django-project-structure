from django.urls import path
from .views import app2_urls

urlpatterns = [   
    path('', app2_urls, name='app2_urls'), 
]