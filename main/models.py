from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Sale(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to={'model__in': ['liquid', 'pod', 'single', 'evaporator']}, verbose_name='Тип предмета')
    object_id = models.PositiveIntegerField(verbose_name='ID проданного предмета')
    item = GenericForeignKey('content_type', 'object_id')
    date = models.DateField(verbose_name='Дата продажи', null=True)
    sold_for = models.PositiveBigIntegerField(verbose_name='Продано за', default=0) 
    created = models.DateField(auto_now_add=True, verbose_name=' Создано')
    updated = models.DateTimeField(auto_now=True, verbose_name=u"Обновлено")
    hidden = models.BooleanField(default=False)
    amount_of_sold = models.IntegerField(default=1, verbose_name='Кол-во раз продано')


    def __str__(self) -> str:
        return f'{self.item} за {self.sold_for}p'

    class Meta:
        verbose_name = 'Продажа'
        verbose_name_plural = 'Продажи'
        ordering = ['-updated']


class LiquidBrand(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название')
    description = models.CharField(max_length=1024, verbose_name='Описание', null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, verbose_name=u"Обновлено")


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бренд Жидкостей'
        verbose_name_plural = 'Бренды Жидкостей'
        ordering = ['-updated']


class Liquid(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название')
    brand = models.ForeignKey(LiquidBrand, on_delete=models.CASCADE, verbose_name='Бренд')
    amount = models.PositiveIntegerField(default=0, verbose_name='Количество')
    price = models.PositiveIntegerField(default=0, verbose_name='Цена')
    margin = models.PositiveIntegerField(default=0, verbose_name='Маржа')
    description = models.CharField(max_length=1024, verbose_name='Описание', null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, verbose_name=u"Обновлено")


    def __str__(self):
        return f'{self.brand} {self.name}'

    class Meta:
        verbose_name = 'Жидкость'
        verbose_name_plural = 'Жидкости'
        ordering = ['-updated']


class PodBrand(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название')
    description = models.CharField(max_length=1024, verbose_name='Описание', null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, verbose_name=u"Обновлено")


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бренд Подов'
        verbose_name_plural = 'Бренды Подов'
        ordering = ['-updated']


class Pod(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название')
    brand = models.ForeignKey(PodBrand, on_delete=models.CASCADE, verbose_name='Бренд')
    amount = models.PositiveIntegerField(default=0, verbose_name='Количество')
    price = models.PositiveIntegerField(default=0, verbose_name='Цена')
    margin = models.PositiveIntegerField(default=0, verbose_name='Маржа')
    battery = models.BooleanField(default=False, verbose_name='АКБ')
    description = models.CharField(max_length=1024, verbose_name='Описание', null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, verbose_name=u"Обновлено")


    def __str__(self):
        return f'{self.brand} {self.name}'

    class Meta:
        verbose_name = 'Под'
        verbose_name_plural = 'Поды'
        ordering = ['-updated']


class SingleBrand(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название')
    description = models.CharField(max_length=1024, verbose_name='Описание', null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, verbose_name=u"Обновлено")


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бренд одноразок'
        verbose_name_plural = 'Бренды одноразок'
        ordering = ['-updated']


class Single(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название')
    brand = models.ForeignKey(SingleBrand, on_delete=models.CASCADE, verbose_name='Бренд')
    amount = models.PositiveIntegerField(default=0, verbose_name='Количество')
    price = models.PositiveIntegerField(default=0, verbose_name='Цена')
    margin = models.PositiveIntegerField(default=0, verbose_name='Маржа')
    description = models.CharField(max_length=1024, verbose_name='Описание', null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, verbose_name=u"Обновлено")


    def __str__(self):
        return f'{self.brand} {self.name}'

    class Meta:
        verbose_name = 'Одноразка'
        verbose_name_plural = 'Одноразки'
        ordering = ['-updated']


class EvaporatorBrand(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название')
    description = models.CharField(max_length=1024, verbose_name='Описание', null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, verbose_name=u"Обновлено")


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бред испариков'
        verbose_name_plural = 'Бренды испариков'
        ordering = ['-updated']


class Evaporator(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название')
    brand = models.ForeignKey(EvaporatorBrand, on_delete=models.CASCADE, verbose_name='Бренд')
    amount = models.PositiveIntegerField(default=0, verbose_name='Количество')
    price = models.PositiveIntegerField(default=0, verbose_name='Цена')
    margin = models.PositiveIntegerField(default=0, verbose_name='Маржа')
    description = models.CharField(max_length=1024, verbose_name='Описание', null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, verbose_name=u"Обновлено")


    def __str__(self):
        return f'{self.brand} {self.name}'

    class Meta:
        verbose_name = 'Испарик'
        verbose_name_plural = 'Испарики'
        ordering = ['-updated']
