# Generated by Django 4.2.1 on 2023-06-09 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_evaporator_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='hidden',
            field=models.BooleanField(default=False),
        ),
    ]
