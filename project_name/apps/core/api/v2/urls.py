from django.urls import path
from .views import core_api_v2_urls

urlpatterns = [
    path('core/', core_api_v2_urls, name='core_api_v2_urls'),
]
