# Generated by Django 4.2.1 on 2023-06-06 23:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('main', '0004_remove_evaporator_sale_remove_liquid_sale_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaporator',
            name='description',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='evaporatorbrand',
            name='description',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='liquid',
            name='description',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='liquidbrand',
            name='description',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='pod',
            name='description',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='podbrand',
            name='description',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='single',
            name='description',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='singlebrand',
            name='description',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Описание'),
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
        ),
    ]
