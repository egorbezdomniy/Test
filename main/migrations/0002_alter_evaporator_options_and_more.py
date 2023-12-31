# Generated by Django 4.2.1 on 2023-06-06 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='evaporator',
            options={'verbose_name': 'Испарик', 'verbose_name_plural': 'Испарики'},
        ),
        migrations.AlterModelOptions(
            name='evaporatorbrand',
            options={'verbose_name': 'Бред испариков', 'verbose_name_plural': 'Бренды испариков'},
        ),
        migrations.AlterModelOptions(
            name='liquid',
            options={'verbose_name': 'Жидкость', 'verbose_name_plural': 'Жидкости'},
        ),
        migrations.AlterModelOptions(
            name='liquidbrand',
            options={'verbose_name': 'Бренд Жидкостей', 'verbose_name_plural': 'Бренды Жидкостей'},
        ),
        migrations.AlterModelOptions(
            name='pod',
            options={'verbose_name': 'Под', 'verbose_name_plural': 'Поды'},
        ),
        migrations.AlterModelOptions(
            name='podbrand',
            options={'verbose_name': 'Бренд Подов', 'verbose_name_plural': 'Бренды Подов'},
        ),
        migrations.AlterModelOptions(
            name='single',
            options={'verbose_name': 'Одноразка', 'verbose_name_plural': 'Одноразки'},
        ),
        migrations.AlterModelOptions(
            name='singlebrand',
            options={'verbose_name': 'Бренд одноразок', 'verbose_name_plural': 'Бренды одноразок'},
        ),
        migrations.AddField(
            model_name='evaporator',
            name='description',
            field=models.CharField(max_length=1024, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='evaporatorbrand',
            name='description',
            field=models.CharField(max_length=1024, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='liquid',
            name='description',
            field=models.CharField(max_length=1024, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='liquidbrand',
            name='description',
            field=models.CharField(max_length=1024, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='pod',
            name='description',
            field=models.CharField(max_length=1024, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='podbrand',
            name='description',
            field=models.CharField(max_length=1024, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='single',
            name='description',
            field=models.CharField(max_length=1024, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='singlebrand',
            name='description',
            field=models.CharField(max_length=1024, null=True, verbose_name='Описание'),
        ),
    ]
