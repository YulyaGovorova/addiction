from rest_framework import serializers
from users.models import User
from users.validators import UserRegisterValidator


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для модели User"""

    class Meta:
        model = User
        fields = '__all__'


class UserRegisterSerializer(serializers.ModelSerializer):
    """Сериализатор для регистрации модели User"""

    password2 = serializers.CharField()

    class Meta:
        model = User
        fields = ['email', 'password', 'password2', 'chat_id']

    def validate(self, data):
        validator = UserRegisterValidator()
        validated_data = validator(data)
        return validated_data

    def save(self, *args, **kwargs):
        user = User(
            email=self.validated_data['email'],
            chat_id=self.validated_data['chat_id'],
            is_superuser=False,
            is_staff=False,
            is_active=True
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({password: "Пароль не совпадает"})
        user.set_password(password)
        user.save()
        return user