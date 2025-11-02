from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ValidationError
from rest_framework import serializers
import re
from .models import NanoBananaCard

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def validate_email(self, value):
        UserModel = get_user_model()
        if UserModel.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with that email already exists.")
        if not re.match(r"[^@]+@[^@]+\.(com|in)$", value):
            raise serializers.ValidationError("Email must contain @ and end with .com or .in")
        return value

    def validate_username(self, value):
        if not value.isalnum():
            raise serializers.ValidationError("Username must be alphanumeric.")
        if len(value) < 5:
            raise serializers.ValidationError("Username must be at least 5 characters long.")
        if not value[0].isalpha():
            raise serializers.ValidationError("Username must start with a letter.")
        return value

    def create(self, validated_data):
        UserModel = get_user_model()
        user = UserModel.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            username=validated_data['username']
        )
        return user

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def check_user(self, validated_data):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=validated_data['email'])
        except UserModel.DoesNotExist:
            raise serializers.ValidationError("No account is associated with this email address.")

        user = authenticate(username=user.username, password=validated_data['password'])
        if not user:
            raise serializers.ValidationError("The password you entered is incorrect.")

        return user

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_new_password = serializers.CharField(required=True)

    def validate(self, data):
        if data['new_password'] != data['confirm_new_password']:
            raise serializers.ValidationError({'new_password': "New passwords must match."})
        return data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username')

class NanoBananaCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = NanoBananaCard
        fields = ('id', 'prompt', 'image', 'created_at')
