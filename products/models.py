from django.db import models

from users.models import User


class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории продуктов'

    def __str__(self):
        return self.name


class Product(models.Model):  # Продукт
    season_list = models.CharField('Сезон:', max_length=30, null=True,)  # Сезон шины
    name = models.CharField('Основные параметры:',max_length=200, null=True)    # Параметры шин или дисков
    image = models.ImageField('Фото:', upload_to='store_db', max_length=200, null=True)  # фото
    thorn = models.CharField('Шипы есть нет:', max_length=6, null=True)    # Шипы есть нет
    code = models.CharField('Код товара:', max_length=20, unique=True, null=True)   # Код товара
    quality = models.CharField('Качество: 0-Новые:',max_length=50, default=0, null=True)  # Качество шины
    rest = models.CharField('Количество на складе:',max_length=5, default=0)   # Количество товара
    model = models.CharField('Модель товара',max_length=50, null=True)  # Модель
    marka = models.CharField('Марка товар',max_length=30, null=True)  # Марка
    color_disk = models.CharField('Цвет диска',max_length=30, null=True)  # Цвет диска
    price_rozn = models.DecimalField('Цена продажи',max_digits=10, decimal_places=0, null=True)  # Цена розница
    price = models.DecimalField('Цена закупа',max_digits=10, decimal_places=0, null=True)  # Цена закупа
    type_list = models.CharField('Тип',max_length=200, null=True)  # Тип шин. Для какой авто
    wrh_list = models.CharField('Склад',max_length=20, null=True)  # Склад Екатеринбург по умолчанию
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE, default=1, null=False)  # Категория Шины или Диски
    description = models.TextField('Описание',max_length=1000, null=True)  # Описание
    modify_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.category.name} | => {self.marka}{self.model} | ' \
               f'Цена: {self.price_rozn} | ' \
               f'Кол-во: {self.rest}шт | ' \
               f'Параметры: ({self.name}) '


class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)


class Basket(models.Model):  # Корзина
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f'Корзина для {self.user.email} | Продукт: {self.product.name}'

    def sum(self):
        return self.product.price_rozn * self.quantity

    def de_json(self):
        basket_item = {
            'product_name': self.product.name,
            'quantity': self.quantity,
            'price': float(self.product.price),
            'sum': float(self.sum()),
        }
        return basket_item

