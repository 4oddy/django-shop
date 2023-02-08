from django.db import models

from users.models import User


class Blog(models.Model):  # Блог
    title = models.CharField('Заголовок записи', max_length=100)
    description = models.TextField('Текст в записи')
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, max_length=100)
    date = models.DateTimeField('Дата публикации')
    img = models.ImageField('Изображение', upload_to='image_blog/')

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def __str__(self):
        return f'{self.title}, {self.author}'


class Comments(models.Model):
    email = models.EmailField()
    name = models.CharField('Имя', max_length=50)
    text_comments = models.TextField('Текст комментария', max_length=5000)
    blog = models.ForeignKey(Blog, verbose_name='Публикация', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.blog}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

