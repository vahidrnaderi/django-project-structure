from django.urls import path
from .views import core_api_v1_urls_views

urlpatterns = [
    path('core/', core_api_v1_urls_views, name='core_api_v1_urls_views'),
]
