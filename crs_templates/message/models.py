from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Message(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор сообщения',
        help_text='Автор'
    )
    text = models.TextField(
        max_length=256,
        verbose_name='Текст сообщения',
        help_text='Текст'
    )
    pub_date = models.DateField(
        auto_now_add=True,
        verbose_name='Дата создания сообщения',
        help_text='Дата'
    )

    class Meta:
        verbose_name ='Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return 'Строковое представление Message'
