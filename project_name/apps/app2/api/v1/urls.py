from django.urls import path
from .views import app2_api_v1_urls

urlpatterns = [
    path('app2/', app2_api_v1_urls, name='app2_api_v1_urls'),
]
