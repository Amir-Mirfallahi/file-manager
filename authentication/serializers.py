from django.db.models import Q
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def validate_email(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError({"email": "This email is already in use."})
        return value

    def create(self, validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')
        # Check if the user with the provided email or username already exists
        if User.objects.filter(Q(username=username) | Q(email=email)).exists():
            raise serializers.ValidationError("User with this email or username already exists.")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=validated_data['password']
        )
        return user

    def update(self, instance, validated_data):
        user = self.context['request'].user
        # Validate if the user is logged in
        if user.pk != instance.pk:
            raise serializers.ValidationError({"authorize": "You dont have permission for this user."})

        instance.set_password(validated_data['password'])
        instance.email = validated_data.get('email', "")
        instance.username = validated_data['username']
        instance.first_name = validated_data.get('first_name', "")
        instance.last_name = validated_data.get('last_name', "")

        instance.save()

        return instance
