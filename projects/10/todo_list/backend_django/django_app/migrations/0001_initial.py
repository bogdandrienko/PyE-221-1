# Generated by Django 4.1.5 on 2023-02-02 15:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, db_index=True, default='', help_text='<small class="text-muted">CharField [0, 300]</small><hr><br>', max_length=300, unique=True, validators=[django.core.validators.MinLengthValidator(0), django.core.validators.MaxLengthValidator(300)], verbose_name='Заголовок')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
                'ordering': ('-title',),
            },
        ),
    ]