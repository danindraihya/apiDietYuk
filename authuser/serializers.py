from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import User

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = [
            'id',
            'username',
            'password',
            'email',
            'height',
            'weight',
            'ttl'
        ]

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = [
            'id',
            'username',
            'height',
            'weight',
            'ttl'
        ]