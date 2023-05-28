import os

from django.apps import AppConfig
from config import settings

class PklotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pklot'

    def ready(self):
        from pklot import set_coordinate
        set_coordinate.initDB()
