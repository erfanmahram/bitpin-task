import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

from core.settings import BASE_DIR

bind = "0.0.0.0:8000"
workers = 1
accesslog = "-"
loglevel = "info"
capture_output = True
enable_stdio_inheritance = True

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
application = get_wsgi_application()
application = WhiteNoise(application, root=os.path.join(BASE_DIR, "staticfiles"))
