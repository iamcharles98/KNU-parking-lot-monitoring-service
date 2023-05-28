from django.apps import AppConfig
from config import settings
import os

class CctvConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "cctv"

    def ready(self):
        if settings.SCHEDULER_DEFAULT and os.environ.get('RUN_MAIN', None) != 'true':
            from cctv import operator
            operator.start()
