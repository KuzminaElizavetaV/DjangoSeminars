import random

from django.core.management.base import BaseCommand
from django.utils import timezone

from seminar2_app.models import User, Product, Order


class Command(BaseCommand):
    help = 'Generate fake authors and post'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count users, orders and product')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for j in range(1, count + 1):
            product = Product(name=f'product{j}',
                              description=f'description{j}',
                              price=random.randint(1, 100),
                              prod_quant=random.randint(1, 10),
                              reg_date=timezone.now())
            product.save()
        for i in range(1, count + 1):
            user = User(name=f'user{i}',
                        email=f'user{i}@mail.com',
                        phone=f'{i}2-12-85-06',
                        address=f'Wall street{i}',
                        reg_date=timezone.now())
            user.save()
        for _ in range(1, count + 1):
            user = User.objects.order_by('?').first()
            for _ in range(1, random.randint(1, count)):
                total_price = 0
                order = Order(customer=user,
                              date_ordered=timezone.now())
                for _ in range(1, random.randint(1, count)):
                    product = Product.objects.order_by('?').first()
                    total_price += product.price
                    order.total_price = total_price
                    order.save()
                    order.products.add(product)
