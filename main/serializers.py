from rest_framework import serializers

from main.models import Habit
from main.validators import validator_habit


class HabitSerializer(serializers.ModelSerializer):
    """ Сериализатор модели Habit """

    class Meta:
        model = Habit
        fields = '__all__'

        validators = [validator_habit]