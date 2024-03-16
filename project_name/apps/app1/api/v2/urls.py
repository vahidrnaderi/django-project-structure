from django.urls import path
from .views import app1_api_v2_urls

urlpatterns = [
    path('app1/', app1_api_v2_urls, name='app1_api_v2_urls'),
]
