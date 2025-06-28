# -*- coding: utf-8 -*-
"""
Модель заполнения цитат
"""

from django.db import models
from django.core.exceptions import ValidationError

class Quote(models.Model):
    # Текст цитаты, должен быть уникальным
    text = models.TextField(unique=True)

    # Источник цитаты
    source = models.CharField(max_length=255)

    # Вес цитаты 
    weight = models.PositiveIntegerField(default=1)

    # Количество лайков и дизлайков
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

    # Дата и время создания
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Уникальность по тексту и источнику
        unique_together = ('text', 'source')

    def clean(self):
        """
        Проверка: У каждого источника должно быть не более 3 цитат
        Вызывается перед сохранением.
        """
        if Quote.objects.filter(source=self.source).count() >= 3 and not self.pk:
            raise ValidationError(f"У источника «{self.source}» уже есть 3 цитаты.")

    def save(self, *args, **kwargs):
        # Запускаем валидацию перед сохранением
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        # Удобное строковое представление объекта
        return f'"{self.text[:50]}" — {self.source}'