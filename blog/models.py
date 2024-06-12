from django.db import models
import os



class Post(models.Model):
    title = models.CharField('Заголовок записа', max_length=100)
    description = models.TextField('Текст записа')
    author = models.CharField('Нік автора', max_length=100)
    date = models.DateField('Дата  публікацій')
    img = models.ImageField("Зображення", upload_to='2024')

    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = 'Запис'
        verbose_name_plural = 'Записи'


class Comments(models.Model):
    email = models.EmailField()
    name = models.CharField("Ім'я", max_length=50)
    text_comments = models.TextField('Текст коментаря', max_length=2000)
    post = models.ForeignKey(Post, verbose_name='Публікація', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.post}'

    class Meta:
        verbose_name = 'Коментар'
        verbose_name_plural = 'Коментарі'


class Likes(models.Model):
    ip = models.CharField('IP-адреса', max_length=100)
    pos = models.ForeignKey(Post, verbose_name='Публікація', on_delete=models.CASCADE)
