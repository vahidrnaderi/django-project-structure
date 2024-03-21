from django.urls import path
from .views import app2_api_v2_urls_views

urlpatterns = [
    path('app2/', app2_api_v2_urls_views, name='app2_api_v2_urls_views'),
]
