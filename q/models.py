

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
#from django.db.models.functions import datetime


class Category(models.Model):
    categories = models.CharField(max_length=200, verbose_name='Категория: ')

    def __unicode__(self):
        return str(self.categories)

    def __str__(self):
        return str(self.categories)
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Post(models.Model):

    def post_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return 'uploads/{0}'.format(filename)

    title = models.CharField(max_length=25, verbose_name='Заголовок поста') # заголовок поста
    description = models.CharField(max_length=100, verbose_name='Краткое описание статьи(необязательно к заполнению)', null=True, blank=True)
    datetime = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True, blank=True, null=True) # дата публикации
    content = models.TextField(verbose_name='Текст поста') # текст поста
    post_cat = models.ForeignKey(Category, on_delete=models.CASCADE, default=False, verbose_name='Категория поста')
    post_likes  = models.IntegerField(verbose_name='Количество лайков', default=0)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    upload = models.ImageField(upload_to=post_path, null=True, blank=True, verbose_name='Добавить изображение')
    AltText = models.CharField(max_length=200, verbose_name='Описание изобрежния', default='')

    def __unicode__(self):
        return str(self.title)

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['-datetime']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Comments(models.Model):

    def comments_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return 'uploads/{0}'.format(filename)

    com_text = models.TextField(max_length=5000, verbose_name='')
    com_posts = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост')
    pubdate = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ComImage = models.ImageField(upload_to=comments_path, null=True, blank=True, verbose_name='Добавить изображение')



    def __str__(self):
        return str(self.com_text)

    def __unicode__(self):
        return str(self.com_text)


class Regulations(models.Model):
    pubdate = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    text = models.TextField(unique=True)
    def __str__(self):
        return str(self.text)

    def __unicode__(self):
        return str(self.text)

    class Meta:
        ordering = ['-pubdate']
        verbose_name = 'Правила'
        verbose_name_plural = 'Правила'


class History(models.Model):
    pubdate = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    text = models.TextField(unique=True)
    def __str__(self):
        return str(self.text)

    def __unicode__(self):
        return str(self.text)

    class Meta:
        ordering = ['-pubdate']
        verbose_name = 'История'
        verbose_name_plural = 'История'


