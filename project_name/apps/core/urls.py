from django.urls import (
    path,
    include
)
from django.views import debug
# from .views import redirect_admin
app_name = "core"

urlpatterns = [

    # Comment next line for real project and uncomment the second line
    path('', debug.default_urlconf),
    # path('', redirect_admin, name='redirect_admin'),

    # Apps urls
    path('', include('project_name.apps.core.urls'), name='core'),
    path('', include('project_name.apps.app1.urls'), name='app1'),
    path('', include('project_name.apps.app2.urls'), name='app2'),

    # path('app1/',
    # include('project_name.apps.app1.urls'),
    # name='app1-urls'),
    # path('app2/',
    # include('project_name.apps.app2.urls'),
    # name='app2-urls'),

    # # REST API v1
    # path('api/v1/',
    # include('project_name.apps.core.api.v1.urls'),
    # name='api-v1-core'),
    # path('api/v1/',
    # include('project_name.apps.app1.api.v1.urls'),
    # name='api-v1-app1'),
    # path('api/v1/',
    # include('project_name.apps.app2.api.v1.urls'),
    # name='api-v1-app2'),

    # # REST API v2
    # path('api/v2/',
    # include('project_name.apps.core.api.v2.urls'),
    # name='api-v2-core'),
    # path('api/v2/',
    # include('project_name.apps.app1.api.v2.urls'),
    # name='api-v2-app1'),
    # path('api/v2/',
    # include('project_name.apps.app2.api.v2.urls'),
    # name='api-v2-app2'),
]
