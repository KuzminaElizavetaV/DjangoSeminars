from random import randint
from django.views.generic import TemplateView, DetailView
from seminar2_app.models import Author, Article


class MainViews(TemplateView):
    template_name = 'seminar3_app/main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context['title'] = 'Главная'
        return context


class AboutViews(TemplateView):
    template_name = 'seminar3_app/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context['title'] = 'Обо мне'
        return context


class GameView(TemplateView):
    template_name = 'seminar3_app/game.html'


class HeadsGame(GameView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        results = [('TAILS', 'HEADS')[randint(0, 1)] for _ in range(self.kwargs['count'])]
        context['results'] = results
        context['title'] = 'Игра в Орел и Решку'
        return context


class DiceGame(GameView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        results = [[randint(1, 6)] for _ in range(self.kwargs['count'])]
        context['results'] = results
        context['title'] = 'Игра в Кости'
        return context


class AllArticlesView(TemplateView):
    template_name = 'seminar3_app/articles.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = Author.objects.get(pk=self.kwargs['id_author'])
        articles = Article.objects.filter(author=author).all()
        context['articles'] = articles
        return context


class DetailArticle(DetailView):
    model = Article
    template_name = 'seminar3_app/detail_article.html'
    context_object_name = 'article'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.show_count += 1
        obj.save()
        return obj
