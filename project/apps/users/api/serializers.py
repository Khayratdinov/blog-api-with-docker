from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from ..models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username', 'email',
            'first_name', 'last_name',
            'bio'
        )


class EmailTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')

    def validate_username(self, value):
        if value == 'me':
            raise ValidationError(message='Bu nomni ishlata olmaysiz iltimos boshqa ism tanlang')
        return value


class TokenObtainPairSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=40, required=True)
    confirmation_code = serializers.CharField(max_length=10, required=True)

    class Meta:
        model = User
        fields = ('username', 'confirmation_code')