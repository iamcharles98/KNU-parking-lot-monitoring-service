from django.apps import AppConfig


class BuildingConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "building"

    def ready(self):
        from pklot import set_coordinate
        set_coordinate.initDB()