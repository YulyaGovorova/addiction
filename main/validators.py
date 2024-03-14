from datetime import timedelta
from rest_framework.serializers import ValidationError


def validator_habit(value):
    """ Проверка заполнения полей привычки """

    time = timedelta(minutes=2)

    if 'is_good' in value and value['is_good']:
        if 'connected_habit' in value or 'prize' in value:
            raise ValidationError('У приятной привычки не может быть связанной привычки или вознаграждения')

    if 'connected_habit' in value and 'prize' in value:
        raise ValidationError('Можно выбрать или приятную привычку или вознаграждение')

    duration = value.get('duration')
    if duration and duration > time:
        raise ValidationError('Привычку можно выполнять не более 2 минут')

    if 'connected_habit' in value:
        if not value['connected_habit'].get('is_good'):
            raise ValidationError('В связанные привычки могут попадать только приятные привычки')