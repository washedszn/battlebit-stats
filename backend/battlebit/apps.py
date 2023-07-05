from django.apps import AppConfig

class BattlebitConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'battlebit'

    def ready(self):
        from .tasks import fetch_and_store_data  # delayed import
        fetch_and_store_data.delay() 
