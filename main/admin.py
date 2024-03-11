from django.contrib import admin

from main.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    """ Привычки в админке """

    list_display = ('name', 'is_public', 'user',)
    list_filter = ('name',)
    search_fields = ('name',)