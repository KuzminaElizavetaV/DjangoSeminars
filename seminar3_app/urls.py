from django.urls import path
from .views import MainViews, AboutViews, HeadsGame, DiceGame, AllArticlesView, DetailView

urlpatterns = [
    path('', MainViews.as_view(), name='main'),
    path('about/', AboutViews.as_view(), name='about'),
    path('heads_game/<int:count>/', HeadsGame.as_view(), name='heads_game'),
    path('dice_game/<int:count>/', DiceGame.as_view(), name='dice_game'),
    path('articles/<int:id_author>/', AllArticlesView.as_view(), name='articles'),
    path('article/<int:pk>/', DetailView.as_view(), name='article'),
]
