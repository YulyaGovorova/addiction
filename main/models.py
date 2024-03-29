from datetime import timedelta

from django.db import models
from config import settings

NULLABLE = {'null': True, 'blank': True}


class Habit(models.Model):
    """ Модель привычки """

    PERIODICTY_CHOICES = (
        (1, 'ежедневно'),
        (2, 'раз в два дня'),
        (3, 'раз в три дня'),
        (4, 'раз в четыре дня'),
        (5, 'раз в пять дней'),
        (6, 'раз в шесть дней'),
        (7, 'раз в семь дней'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='владелец')
    name = models.CharField(max_length=100, verbose_name='название привычки')
    place = models.CharField(max_length=100, **NULLABLE, verbose_name='место выполнения привычки')
    time = models.TimeField(**NULLABLE, verbose_name='время выполнения привычки')
    action = models.CharField(max_length=100, verbose_name='действие привычки')
    is_good = models.BooleanField(default=True, verbose_name='признак приятной привычки')
    connected_habit = models.ForeignKey('self', on_delete=models.CASCADE, **NULLABLE, verbose_name='связанная привычка')
    period = models.PositiveSmallIntegerField(choices=PERIODICTY_CHOICES, default='1',
                              verbose_name='периодичность привычки')
    duration = models.DurationField(default=timedelta(minutes=2),
                                    verbose_name='продолжительность выполнения привычки')
    is_public = models.BooleanField(default=True, verbose_name='признак публичной привычки')
    prize = models.CharField(max_length=100, verbose_name='награда', **NULLABLE)
    useful = models.BooleanField(default=False, verbose_name='признак полезная привычка')

    def __str__(self):
        return f'Пользователь: {self.user} - привычка: {self.name}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
        ordering = ('name',)
