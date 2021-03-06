# Generated by Django 2.2.10 on 2020-08-13 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('url', models.CharField(max_length=1000, verbose_name='Ссылка')),
                ('image', models.ImageField(upload_to='', verbose_name='Картинка')),
            ],
        ),
    ]
