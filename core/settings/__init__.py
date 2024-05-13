import os

APP_MODE = os.getenv("APP_ENV")

if APP_MODE == "production":
    from .base import *

else:
    from .staging import *
