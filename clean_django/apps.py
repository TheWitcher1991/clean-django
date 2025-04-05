from django.apps import AppConfig


class RestFrameworkConfig(AppConfig):
    name = "clean_django"
    verbose_name = "Clean Django"

    def ready(self):
        pass
