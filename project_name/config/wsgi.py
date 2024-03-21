"""
WSGI config for project_name project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

if os.getenv('ENVIRONMENT') == 'production':
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_name.config.settings.production')
        print(f'--> Running manage.py with production environment: {sys.argv}')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_name.config.settings.development')
    print(f'--> Running manage.py with development environment: {sys.argv}')


application = get_wsgi_application()
