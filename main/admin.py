from django.contrib import admin

from main.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    """ Привычки в админке """

    list_display = ('name', 'is_public', 'user', 'useful')
    list_filter = ('name', 'useful')
    search_fields = ('name',)