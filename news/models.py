from django.db import models


class News(models.Model):

    class Meta:
        verbose_name = 'новость '
        verbose_name_plural = 'новости'

    name = models.CharField(max_length=100, verbose_name='заголовок')
    image = models.ImageField(verbose_name='изображение', upload_to='news_images/', null=True)
    description = models.CharField(max_length=250, verbose_name='краткое описание')
    content = models.TextField(verbose_name='контент')
    date = models.DateTimeField(verbose_name='дата добавление')
    is_published = models.BooleanField(default=True, verbose_name='публичность')

    def __str__(self):
        return f'{self.name} - {self.date}'


class Category(models.Model):

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    name = models.CharField(verbose_name='название', max_length=50)

    def __str__(self):
        return f'{self.name}'

# Create your models here.
