from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser("admin", "abhishekjain118@gmail.com", "admin")
        else:
            self.stdout.write("this username already exists", ending='')