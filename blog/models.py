from django.db import models

class Post(models.Model):
    title = models.CharField('Заговолок поста', max_length=100)
    description = models.TextField('Опис поста')
    author = models.CharField('Нік автора', max_length=100)
    date = models.DateField('Дата публікації') 

    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = 'Запис'
        verbose_name_plural = 'Записи'
