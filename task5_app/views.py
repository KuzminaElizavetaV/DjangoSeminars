import logging
import random
from django.http import HttpResponse

logger = logging.getLogger(__name__)

# Задание №4
# 📌 Создайте представление “Привет, мир!” внутри вашего первого приложения.
# 📌 Настройте маршруты


def index(request):
    logger.info('Index page accessed')
    return HttpResponse('Hello, world!')


# Задание №5
# 📌 Создайте новое приложение. Подключите его к проекту. В приложении должно быть три простых представления,
# возвращающих HTTP ответ:
# 📌 Орёл или решка
# 📌 Значение одной из шести граней игрального кубика
# 📌 Случайное число от 0 до 100
# 📌 Пропишите маршруты


def one(request):
    answer = random.choice(['Орел', 'Решка'])
    logger.info(f'Выпало: <<{answer}>>')
    return HttpResponse(f'Орёл или решка? => <<{answer}!>>')


def two(request):
    answer = random.randint(1, 6)
    logger.info(f'Значение одной из шести граней игрального кубика => {answer}')
    return HttpResponse(f'Значение одной из шести граней игрального кубика => {answer}')


def three(request):
    answer = random.randint(0, 100)
    logger.info(f'Случайное число от 0 до 100 => <<{answer}>>')
    return HttpResponse(f'Случайное число от 0 до 100 => <<{answer}>>')
