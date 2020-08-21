from django.db import models


class Film(models.Model):
    name = models.CharField('Название', max_length=64, null=True, blank=True)
    description = models.TextField('Описание', null=True, blank=True)
    url = models.CharField('Ссылка', max_length=1000, null=True, blank=True)
    image = models.CharField('Картинка', max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'