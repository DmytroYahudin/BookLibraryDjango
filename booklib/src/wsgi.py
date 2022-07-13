"""
WSGI config for src project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

if os.environ.get('DOCKER_DEVELOPMENT'):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.docker_settings')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')

application = get_wsgi_application()
