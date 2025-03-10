from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError
from django.utils import timezone


class Status(models.Model):
    name = models.CharField(max_length=50, unique=True)
    key = models.CharField(primary_key=True, max_length=50)

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    def __str__(self):
        return self.name


class TypeCashFlow(models.Model):
    name = models.CharField(max_length=50, unique=True)
    key = models.CharField(primary_key=True, max_length=50)


    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

    def __str__(self):
        return self.name


class Category(models.Model):
    type = models.ForeignKey(TypeCashFlow, on_delete=models.CASCADE, verbose_name='Тип')
    name = models.CharField(max_length=50, unique=True)
    key = models.CharField(primary_key=True, max_length=50)


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.type} → {self.name}'


class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    name = models.CharField(max_length=50)
    key = models.CharField(primary_key=True, max_length=50)


    class Meta:
        unique_together = ('category', 'name')
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return f'{self.category} → {self.name}'


class CashFlow(models.Model):
    created_at = models.DateTimeField(verbose_name='Дата создания записи', default=timezone.now)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name='Статус')
    type_cash_flow = models.ForeignKey(TypeCashFlow, on_delete=models.PROTECT, verbose_name='Тип')
    category_cash_flow = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    subcategory_cash_flow = models.ForeignKey(Subcategory, on_delete=models.PROTECT, verbose_name='подкатегория')
    amount = models.DecimalField(verbose_name='Сумма', max_digits=10, decimal_places=2)
    comment = models.TextField(verbose_name='Комментарий', blank=True)

    def clean(self):
        if self.subcategory_cash_flow and self.subcategory_cash_flow.category != self.category_cash_flow:
            raise ValidationError({
                'subcategory_cash_flow': 'Подкатегория должна принадлежать выбранной категории.'
            })
        if self.category_cash_flow and self.category_cash_flow.type != self.type_cash_flow:
            raise ValidationError({
                'category_cash_flow': 'Категория должна принадлежать выбранному типу.'
            })

    class Meta:
        verbose_name = 'Движение денежных средств'
        verbose_name_plural = 'Движения денежных средств'
