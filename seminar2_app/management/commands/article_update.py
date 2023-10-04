from django.core.management.base import BaseCommand

from seminar2_app.models import Article


class Command(BaseCommand):
    help = "Update article"

    def add_arguments(self, parser):
        parser.add_argument('article_id', type=str, help='Article id')
        parser.add_argument('title', type=str, help='Article title')

    def handle(self, *args, **kwargs):
        article_id = kwargs.get('article_id')
        title = kwargs.get('title')
        article = Article.objects.filter(id=article_id).first()
        article.title = title
        article.save()
        self.stdout.write(f'{article}')
