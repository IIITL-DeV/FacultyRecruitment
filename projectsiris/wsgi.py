"""
WSGI config for projectSIRIS project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from dotenv import load_dotenv

project_folder = os.path.expanduser(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv(os.path.join(project_folder, '.env'))
# print("folder: ",os.path.join(project_folder, '.env'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projectsiris.settings')

application = get_wsgi_application()
