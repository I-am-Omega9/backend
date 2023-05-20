from django.db import models


class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,verbose_name='Имя')
    email = models.EmailField(unique=True,verbose_name='Почта')
    text = models.TextField(verbose_name='Текст')
    date = models.DateTimeField(auto_now_add=True)



class Users(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


