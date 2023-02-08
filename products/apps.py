from django.apps import AppConfig

from .scheduler import start_work


class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'

    def ready(self):
        start_work(minutes=60)
