from django.core.management.base import BaseCommand

from seminar2_app.models import User


class Command(BaseCommand):
    help = "Update user"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=str, help='Author id')
        parser.add_argument('email', type=str, help='Author email')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        email = kwargs.get('email')
        user = User.objects.filter(id=pk).first()
        user.email = email
        user.save()
        self.stdout.write(f'{user}')
