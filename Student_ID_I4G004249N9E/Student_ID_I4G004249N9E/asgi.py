"""
ASGI config for Student_ID_I4G004249N9E project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Student_ID_I4G004249N9E.settings')

application = get_asgi_application()
