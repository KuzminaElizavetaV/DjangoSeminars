from django.core.management.base import BaseCommand
from django.utils import timezone

from seminar2_app.models import Author, Article


class Command(BaseCommand):
    help = 'Generate fake authors and post'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count users')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            author = Author(f_name=f'f_name{i}', l_name='un name', email=f'user{i}@mail.com', biography='About',
                            birthday='2023-09-21')
            author.save()
            for j in range(1, count + 1):
                article = Article(author=author,
                                  title=f'Title_{j}',
                                  content=f'Text from {author.f_name} #_{j} is bla bla bla many long text',
                                  published=timezone.now(),
                                  category='category',
                                  show_count='1',
                                  is_published=True)
                article.save()
