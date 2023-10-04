from django.core.management.base import BaseCommand
from django.utils import timezone

from seminar2.models import User


class Command(BaseCommand):
    help = "Create user"

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='User name')

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        user = User(name=name,
                    email='user@mail.com',
                    phone='2-12-85-06',
                    address='Wall street',
                    reg_date=timezone.now())
        user.save()
        self.stdout.write(f'{user}')
