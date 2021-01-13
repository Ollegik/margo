from django.db import models

class Articles(models.Model):
    title= models.CharField('Название фильма', max_length=100)
    story = models.TextField('Сюжет')
    data = models.DateField('Дата выхода')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/margo/{self.id}'


    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

class Answer(models.Model):
    article = models.ForeignKey(
        'Articles', on_delete=models.CASCADE, verbose_name='Фильм')
    text = models.TextField(verbose_name='Отзыв')

    def __str__(self):
        return self.article.title

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'