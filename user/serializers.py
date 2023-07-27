from rest_framework import serializers
from .models import Profile
from django.contrib.auth import get_user_model

User = get_user_model


# class ProfileSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Profile
#         fields = ['image', 'nickname', 'introduce', 'created_at', 'updated_at']


class UserSerializer(serializers.ModelSerializer):
    # profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['email', 'password']
