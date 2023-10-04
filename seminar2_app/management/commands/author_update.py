from django.core.management.base import BaseCommand

from seminar2_app.models import Author


class Command(BaseCommand):
    help = "Update author"

    def add_arguments(self, parser):
        parser.add_argument('author_id', type=str, help='Author id')
        parser.add_argument('email', type=str, help='Author email')

    def handle(self, *args, **kwargs):
        author_id = kwargs.get('author_id')
        email = kwargs.get('email')
        author = Author.objects.filter(id=author_id).first()
        author.email = email
        author.save()
        self.stdout.write(f'{author}')
