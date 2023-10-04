from django.core.management.base import BaseCommand

from seminar2_app.models import User


class Command(BaseCommand):
    help = "Get user by id"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=str, help='User id')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('author_id')
        user = User.objects.filter(id=pk).first()
        self.stdout.write(f'{user}')
