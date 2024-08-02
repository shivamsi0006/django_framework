from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model=models.UserProfile
        fields=('id','email','name','password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type':'password'}
            }
        }

    def create(self,valiidated_data):
        user=models.UserProfile.objects.create_user(
            email=valiidated_data['email'],
            name=valiidated_data['name'],
            password=valiidated_data['password']

        )

        return user