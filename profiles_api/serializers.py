from rest_framework import serializers

from profiles_api import models


class NameSerializer(serializers.Serializer):
    """serializes name field for our ApiView"""
    name = serializers.CharField(max_length=50)


class UserProfileSerializer(serializers.ModelSerializer):
    """serializes a user profile object"""
    class Meta:
        model = models.UserProfile
        fields = ('id', 'name', 'email', 'password')

        extra_kwargs = {
            'password' : {
                'write_only' : True,
                'style' : {
                    'input_type' :'password',
                },
            }
        }


    def create(self, validated_data):
        """creates and returns a new user"""
        user = models.UserProfile.objects.create_user(
            name = validated_data['name'],
            email = validated_data['email'],
            password = validated_data['password'],
        )

        return user