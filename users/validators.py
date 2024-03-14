from rest_framework import serializers

class UserRegisterValidator:
    def __call__(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        password2 = attrs.get('password2')
        chat_id = attrs.get('chat_id')

        if not email:
            raise serializers.ValidationError({'email': 'Электронная почта обязательна'})

        if not password or not password2:
            raise serializers.ValidationError({'password': 'Пароль и подтверждение пароля обязательны'})

        if password != password2:
            raise serializers.ValidationError({'password': 'Пароли не совпадают'})

        if len(password) < 8:
            raise serializers.ValidationError({'password': 'Пароль должен содержать не менее 8 символов'})

        if not chat_id:
            raise serializers.ValidationError({'chat_id': 'Идентификатор чата обязателен'})

        return attrs