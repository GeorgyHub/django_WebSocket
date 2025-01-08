from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class message(models.Model):
    text = models.CharField(max_length=150, null=True, blank=False, verbose_name='Сообщение')
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, default=None, blank=True, verbose_name='Пользователь')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')