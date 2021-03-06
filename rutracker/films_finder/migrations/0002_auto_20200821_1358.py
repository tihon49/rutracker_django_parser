# Generated by Django 2.2.10 on 2020-08-21 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films_finder', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='film',
            options={'verbose_name': 'Фильм', 'verbose_name_plural': 'Фильмы'},
        ),
        migrations.AlterField(
            model_name='film',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='film',
            name='image',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='film',
            name='name',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='film',
            name='url',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Ссылка'),
        ),
    ]
