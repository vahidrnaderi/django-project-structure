from django.urls import path
from .views import app2_api_v2_urls

urlpatterns = [
    path('app2/', app2_api_v2_urls, name='app2_api_v2_urls'),
]
