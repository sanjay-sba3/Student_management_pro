from rest_framework import serializers
from ..models.user import User

class UserSerializer(serializers.ModelSerializer):
    role_name = serializers.CharField(source='role.role')

    class Meta:
        model = User
        # fields = '__all__'
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email', 'role_name']


class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password']        