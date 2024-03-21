"""
ASGI config for project_name project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
import sys

from django.core.asgi import get_asgi_application

if os.getenv('ENVIRONMENT') == 'production':
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_name.config.settings.production')
        print(f'--> Running manage.py with production environment: {sys.argv}')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_name.config.settings.development')
    print(f'--> Running manage.py with development environment: {sys.argv}')

application = get_asgi_application()
