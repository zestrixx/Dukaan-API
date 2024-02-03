from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import CustomUser
# User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
    required=True,
    validators=[UniqueValidator(queryset=User.objects.all())]
  )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True, required=True)


    class Meta:
        model = User
        fields = ('first_name', 'last_name','username', 'password', 'confirm_password')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError(
            {"password": "Password fields didn't match."})
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()