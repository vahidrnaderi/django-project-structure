from django.urls import path
from .views import core_api_v1_urls

urlpatterns = [
    path('core/', core_api_v1_urls, name='core_api_v1_urls'),
]
