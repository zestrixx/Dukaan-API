from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
User = get_user_model() #Return the User model that is active in this project - CustomUser in this case.

class UserRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name','email', 'password', 'confirm_password')
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
        #~we have to remove the 'confirm_password' field from validated data ordered dict before creating user object as user doesn't have confirm_password field in the custom user model as it is used for frontend purpose only to let user input correct password.
        validated_data.pop('confirm_password', None)
        password = validated_data.pop('password', None)
        #& we can always create user without popping out password before creation but that way we django will not hashes the password, so I first popped the password and created the user obj then set the password using set_password() method to ensure hashing
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()