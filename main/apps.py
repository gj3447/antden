from django.apps import AppConfig
import sys
class MainConfig(AppConfig):
    name = 'main'
    verbose_name = 'My App'

    def ready(self):
        if 'runserver' not in sys.argv:
            return True
        from . import database
        database.start()

        
        
