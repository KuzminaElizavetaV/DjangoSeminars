"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from seminar2_app import views

comment_patterns = [
    path('', views.comment_read, name='comments'),
    path('create/', views.comment_create, name='comment_create'),
    path('update/', views.comment_update, name='comment_update'),
    path('delete/', views.comment_delete, name='comment_delete'),
    path('comment_by_author/', views.comment_by_author, name='comment_by_author'),
    path('comment_by_article/', views.comment_by_article, name='comment_by_article'),
]

article_patterns = [
    path('', views.article_read, name='articles'),
    path('create/', views.article_create, name='article_create'),
    path('update/', views.article_update, name='article_update'),
    path('delete/', views.article_delete, name='article_delete'),
    path('article_by_author/', views.article_by_author, name='article_by_author'),
]

users_patterns = [
    path('', views.user_read, name='users'),
    path('create/', views.user_create, name='user_create'),
    path('update/', views.user_update, name='user_update'),
    path('delete/', views.user_delete, name='user_delete'),
]

products_patterns = [
    path('', views.product_read, name='products'),
    path('create/', views.product_create, name='product_create'),
    path('update/', views.product_update, name='product_update'),
    path('delete/', views.product_delete, name='product_delete'),
]

orders_patterns = [
    path('', views.order_read, name='orders'),
    path('create/', views.order_create, name='order_create'),
    path('update/', views.order_update, name='order_update'),
    path('delete/', views.order_delete, name='order_delete'),
]

urlpatterns = [
    path('', views.seminar2, name='seminar2'),
    path('heads_tails/', views.heads_tails, name='heads_tails'),
    path('comments/', include(comment_patterns)),
    path('articles/', include(article_patterns)),
    path('users/', include(users_patterns)),
    path('products/', include(products_patterns)),
    path('orders/', include(orders_patterns)),
    path('authors/', views.author_read, name='authors'),
]
