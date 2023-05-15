from rest_framework import serializers


class NameSerializer(serializers.Serializer):
    """serializes name field for our ApiView"""
    name = serializers.CharField(max_length=50)
