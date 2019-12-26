from django.apps import AppConfig


class MatirbankConfig(AppConfig):
    name = 'matirbank'

    def ready(self):
        import matirbank.signals.hooks

        super().ready()


