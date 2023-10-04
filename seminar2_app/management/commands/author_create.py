from django.core.management.base import BaseCommand

from seminar2_app.models import Author


class Command(BaseCommand):
    help = "Create author"

    def add_arguments(self, parser):
        parser.add_argument('f_name', type=str, help='Author name')

    def handle(self, *args, **kwargs):
        f_name = kwargs.get('f_name')
        author = Author(f_name=f_name, l_name='unname', email='user@mail.com', biography='About', birthday='2023-09-21')
        author.save()
        self.stdout.write(f'{author}')
        