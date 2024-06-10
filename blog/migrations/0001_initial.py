# Generated by Django 4.2.8 on 2024-06-10 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заговолок поста')),
                ('description', models.TextField(verbose_name='Опис поста')),
                ('author', models.CharField(max_length=100, verbose_name='Нік автора')),
                ('date', models.DateField(verbose_name='Дата публікації')),
            ],
            options={
                'verbose_name': 'Запис',
                'verbose_name_plural': 'Записи',
            },
        ),
    ]
