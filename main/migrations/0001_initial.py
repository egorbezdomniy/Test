# Generated by Django 4.2.1 on 2023-06-06 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EvaporatorBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='LiquidBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='PodBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='SingleBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='Single',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название')),
                ('amount', models.PositiveIntegerField(default=0, verbose_name='Количество')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Цена')),
                ('margin', models.PositiveIntegerField(default=0, verbose_name='Маржа')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.liquidbrand', verbose_name='Бренд')),
            ],
        ),
        migrations.CreateModel(
            name='Pod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название')),
                ('amount', models.PositiveIntegerField(default=0, verbose_name='Количество')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Цена')),
                ('margin', models.PositiveIntegerField(default=0, verbose_name='Маржа')),
                ('battery', models.BooleanField(default=False, verbose_name='АКБ')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.liquidbrand', verbose_name='Бренд')),
            ],
        ),
        migrations.CreateModel(
            name='Liquid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название')),
                ('amount', models.PositiveIntegerField(default=0, verbose_name='Количество')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Цена')),
                ('margin', models.PositiveIntegerField(default=0, verbose_name='Маржа')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.liquidbrand', verbose_name='Бренд')),
            ],
        ),
        migrations.CreateModel(
            name='Evaporator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название')),
                ('amount', models.PositiveIntegerField(default=0, verbose_name='Количество')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Цена')),
                ('margin', models.PositiveIntegerField(default=0, verbose_name='Маржа')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.liquidbrand', verbose_name='Бренд')),
            ],
        ),
    ]
