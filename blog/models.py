from django.db import models

class Post(models.Model):
    title = models.CharField('Заговолок поста', max_length=100)
    description = models.TextField('Опис поста')
    author = models.CharField('Нік автора', max_length=100)
    date = models.DateField('Дата публікації') 
    img = models.ImageField('Зображення', upload_to='img/%Y')
    
    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = 'Запис'
        verbose_name_plural = 'Записи'

class Comments(models.Model):
    email = models.EmailField()
    name = models.CharField("ім'я", max_length=50 )
    text_comments = models.TextField('Текст коментаря', max_length=2000)
    post = models.ForeignKey(Post, verbose_name='Публцікація', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.post}'

    class Meta:
        verbose_name = 'Коментар'
        verbose_name_plural = 'Коментарі'