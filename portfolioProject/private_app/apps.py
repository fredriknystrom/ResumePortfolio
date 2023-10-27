from django.apps import AppConfig


class PrivateAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'private_app'
