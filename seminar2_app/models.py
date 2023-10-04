from django.db import models
from django.urls import reverse


class HeadsTails(models.Model):
    res_time = models.DateTimeField()
    res = models.CharField(max_length=50)

    @staticmethod
    def statistic(n):
        n = int(n)
        dict_res = {"Орел": 0, "Решка": 0}
        query = list(HeadsTails.objects.all())
        list_res = query[-n:]
        for item in list_res:
            if "Орел" in str(item):
                dict_res["Орел"] += 1
            elif "Решка" in str(item):
                dict_res["Решка"] += 1
        return dict_res

    def __str__(self):
        return f'  time: {self.res_time}, res: {self.res}  '


class Author(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField()
    birthday = models.DateField()
    fullname = f'{f_name} {l_name}'

    def __str__(self):
        return f'  first name: {self.f_name}, last name: {self.l_name}  '


class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    published = models.DateTimeField()
    category = models.CharField(max_length=200)
    show_count = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('article', kwargs={'pk': self.pk})

    def __str__(self):
        return f'Title is {self.title}, author is {self.author}'


class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.TextField()
    published = models.DateTimeField()
    updated = models.DateTimeField()

    def __str__(self):
        return f'Title is {self.comment}'


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    reg_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'User: {self.name}<br>'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    prod_quant = models.IntegerField()
    reg_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Product: {self.name}, price: {self.price}<br>'


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Order # {self.pk}, total price: {self.total_price}<br>'
