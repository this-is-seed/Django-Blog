from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def apps(self):
    	import users.signals