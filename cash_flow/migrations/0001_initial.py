# Generated by Django 5.1.6 on 2025-03-08 15:23

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TypeCashFlow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cash_flow.category', verbose_name='Категория')),
            ],
        ),
        migrations.CreateModel(
            name='CashFlow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(default=datetime.datetime.now, verbose_name='Дата создания записи')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Сумма')),
                ('comment', models.TextField(blank=True, verbose_name='Комментарий')),
                ('category_cash_flow', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cash_flow.category', verbose_name='Категория')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cash_flow.status', verbose_name='Статус')),
                ('subcategory_cash_flow', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cash_flow.subcategory', verbose_name='подкатегория')),
                ('type_cash_flow', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cash_flow.typecashflow', verbose_name='Тип')),
            ],
        ),
    ]
