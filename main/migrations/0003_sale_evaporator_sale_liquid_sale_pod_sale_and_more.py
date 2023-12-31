# Generated by Django 4.2.1 on 2023-06-06 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('main', '0002_alter_evaporator_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата')),
                ('actual_price', models.PositiveIntegerField(verbose_name='Продано за')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype')),
            ],
            options={
                'verbose_name': 'Продажа',
                'verbose_name_plural': 'Продажи',
            },
        ),
        migrations.AddField(
            model_name='evaporator',
            name='sale',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='evaporators', to='main.sale', verbose_name='Продажа'),
        ),
        migrations.AddField(
            model_name='liquid',
            name='sale',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='liquids', to='main.sale', verbose_name='Продажа'),
        ),
        migrations.AddField(
            model_name='pod',
            name='sale',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pods', to='main.sale', verbose_name='Продажа'),
        ),
        migrations.AddField(
            model_name='single',
            name='sale',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='singles', to='main.sale', verbose_name='Продажа'),
        ),
    ]
