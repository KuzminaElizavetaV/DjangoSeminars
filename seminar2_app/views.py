import logging
import random
from django.utils import timezone
from django.http import HttpResponse
from seminar2_app.models import HeadsTails, Author, Article, Comment, User, Product, Order

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, filename='logger.log', filemode='a', format='%(levelname)s %(message)s')


def seminar2(request):
    logger.info(f'{request} request received')
    return HttpResponse('<h1>Seminar2</h1>')


def heads_tails(request):
    logger.info(f'{request} request received')
    n = request.GET.get("n", "5")  # ?n=10
    res = random.choice(['Орел', 'Решка'])
    res_w = HeadsTails(res_time=timezone.now(), res=res)
    HeadsTails.save(res_w)
    data = HeadsTails.statistic(n)
    print(data.items())
    return HttpResponse(data.items())


def author_read(request):
    logger.info(f'{request} request received')
    author = Author.objects.all()
    return HttpResponse(author)


def article_read(request):
    logger.info(f'{request} request received')
    article = Article.objects.all()
    return HttpResponse(article)


def article_by_author(request):
    logger.info(f'{request} request received')
    name = request.GET.get('name')
    author_id = Author.objects.filter(f_name=name).first().id
    articles = Article.objects.filter(author_id=author_id).all()
    return HttpResponse(articles)


def article_create(request):
    logger.info(f'{request} request received')
    author_id = request.GET.get('author_id')
    author = Author.objects.filter(id=author_id).first()
    article = Article(author=author,
                      title='title',
                      content='comment text',
                      published=timezone.now(),
                      category='category',
                      show_count=1,
                      is_published=True)
    article.save()
    return HttpResponse(article)


def article_update(request):
    logger.info(f'{request} request received')
    article_id = request.GET.get('article_id')
    article = Article.objects.filter(id=article_id).first()
    article.title = 'new_title'
    article.content = 'new_content'
    article.save()
    return HttpResponse(article)


def article_delete(request):
    logger.info(f'{request} request received')
    article_id = request.GET.get('article_id')
    article = Article.objects.filter(id=article_id).first()
    article.delete()
    return HttpResponse(article)


def comment_read(request):
    logger.info(f'{request} request received')
    comment = Comment.objects.all()
    return HttpResponse(comment)


def comment_by_author(request):
    logger.info(f'{request} request received')
    name = request.GET.get('name')
    author_id = Author.objects.filter(f_name=name).first().id
    comments = Comment.objects.filter(author_id=author_id).all()
    return HttpResponse(comments)


def comment_by_article(request):
    logger.info(f'{request} request received')
    name = request.GET.get('name')
    article_id = Article.objects.filter(title=name).first().id
    comments = Comment.objects.filter(article_id=article_id).all()
    return HttpResponse(comments)


def comment_create(request):
    logger.info(f'{request} request received')
    author_id = request.GET.get('author_id')
    article_id = request.GET.get('article_id')
    author = Author.objects.filter(id=author_id).first()
    article = Article.objects.filter(id=article_id).first()
    comment = Comment(author=author,
                      article=article,
                      comment='comment text',
                      published=timezone.now(),
                      updated=timezone.now(), )
    comment.save()
    return HttpResponse(comment)


def comment_update(request):
    logger.info(f'{request} request received')
    comment_id = request.GET.get('comment_id')
    comment = Comment.objects.filter(id=comment_id).first()
    comment.comment = 'new_comment'
    comment.save()
    return HttpResponse(comment)


def comment_delete(request):
    logger.info(f'{request} request received')
    comment_id = request.GET.get('comment_id')
    comment = Comment.objects.filter(id=comment_id).first()
    comment.delete()
    return HttpResponse(comment)


def user_read(request):
    logger.info(f'{request} request received')
    user = User.objects.all()
    return HttpResponse(user)


def user_create(request):
    logger.info(f'{request} request received')
    user_name = request.GET.get('name')
    user = User(name=user_name,
                email=f'{user_name}@mail.com',
                phone=f'2-12-85-06',
                address=f'Wall street',
                reg_date=timezone.now())
    user.save()
    return HttpResponse(user)


def user_update(request):
    logger.info(f'{request} request received')
    user_id = request.GET.get('user_id')
    user = User.objects.filter(id=user_id).first()
    user.name = 'new_user_name'
    user.save()
    return HttpResponse(user)


def user_delete(request):
    logger.info(f'{request} request received')
    user_id = request.GET.get('user_id')
    user = Comment.objects.filter(id=user_id).first()
    user.delete()
    return HttpResponse(user)


def product_read(request):
    logger.info(f'{request} request received')
    product = Product.objects.all()
    return HttpResponse(product)


def product_create(request):
    logger.info(f'{request} request received')
    product_name = request.GET.get('name')
    product = Product(name=product_name,
                      description=f'{product_name} description',
                      price=random.randint(1, 100),
                      prod_quant=random.randint(1, 10),
                      reg_date=timezone.now())
    product.save()
    return HttpResponse(product)


def product_update(request):
    logger.info(f'{request} request received')
    product_id = request.GET.get('product_id')
    product = Product.objects.filter(id=product_id).first()
    product.name = 'new_product'
    product.save()
    return HttpResponse(product)


def product_delete(request):
    logger.info(f'{request} request received')
    product_id = request.GET.get('product_id')
    product = Product.objects.filter(id=product_id).first()
    product.delete()
    return HttpResponse(product)


def order_read(request):
    logger.info(f'{request} request received')
    order = Order.objects.all()
    return HttpResponse(order)


def order_create(request):
    logger.info(f'{request} request received')
    user_id = request.GET.get('user_id')
    product_id = request.GET.get('product_id')
    user = Order.objects.filter(id=user_id).first()
    product = Order.objects.filter(id=product_id).first()
    order = Order(customer=user,
                  products=product,
                  total_price=product.price,
                  date_ordered=timezone.now())
    order.save()
    return HttpResponse(order)


def order_update(request):
    logger.info(f'{request} request received')
    order_id = request.GET.get('order_id')
    user_id = request.GET.get('user_id')
    order = Order.objects.filter(id=order_id).first()
    order.customer = user_id
    order.save()
    return HttpResponse(order)


def order_delete(request):
    logger.info(f'{request} request received')
    order_id = request.GET.get('order_id')
    order = Order.objects.filter(id=order_id).first()
    order.delete()
    return HttpResponse(order)
