from django.core.management.base import BaseCommand
from django.utils import timezone
from seminar2_app.models import Author, Article


class Command(BaseCommand):
    help = "Create article"

    def add_arguments(self, parser):
        parser.add_argument('author_id', type=str, help='Author id')
        parser.add_argument('title', type=str, help='Article title')

    def handle(self, *args, **kwargs):
        author_id = kwargs.get('author_id')
        author = Author.objects.filter(id=author_id).first()
        title = kwargs.get('title')
        article = Article(author=author,
                          title=title,
                          content='content',
                          published=timezone.now(),
                          category='category',
                          show_count='1',
                          is_published=True)
        article.save()
        self.stdout.write(f'{article}')
        