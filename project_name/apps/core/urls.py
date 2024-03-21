from django.urls import (
    path,
    include,
)
from django.views import debug
from .views import core_urls_views
from .constants import (
    API_V1_PATH,
    API_V2_PATH,
)
# from .views import redirect_admin

app_name = "core"

urlpatterns = [

    # Comment next line for real project and uncomment the second line
    path('', debug.default_urlconf),
    path('core/', core_urls_views, name='core_urls_views'),
    # path('', redirect_admin, name='redirect_admin'),

    # path('app1/',
    # include('project_name.apps.app1.urls'),
    # name='app1-urls'),
    # path('app2/',
    # include('project_name.apps.app2.urls'),
    # name='app2-urls'),

    # REST API v1
    path(API_V1_PATH,
    include('project_name.apps.core.api.v1.urls'),
    name='core_api_v1_urls'),
    path(API_V1_PATH,
    include('project_name.apps.app1.api.v1.urls'),
    name='app1_api_v1_urls'),
    path(API_V1_PATH,
    include('project_name.apps.app2.api.v1.urls'),
    name='app2_api_v1_urls'),

    # REST API v2
    path(API_V2_PATH,
    include('project_name.apps.core.api.v2.urls'),
    name='core_api_v2_urls'),
    path(API_V2_PATH,
    include('project_name.apps.app1.api.v2.urls'),
    name='app1_api_v2_urls'),
    path(API_V2_PATH,
    include('project_name.apps.app2.api.v2.urls'),
    name='app2_api_v2_urls'),
]
