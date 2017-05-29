from rest_framework import serializers
from django.db import models
from .models import User
from rest_framework.response import Response
from rest_framework import status

class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    id = serializers.UUIDField()

    class Meta:
        model = User # we need to tell which model we are using
        fields = ('first_name', 'last_name', 'id')
    #
    # def create(self, validated_data):
    #     return User.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):  # for put method
    #     """
    #     Update and return an existing `Snippet` instance, given the validated data.
    #     """
    #     instance.first_name = validated_data.get('first_name', instance.first_name)
    #     instance.last_name = validated_data.get('last_name', instance.last_name)
    #     instance.save()
    #     return instance

    def validate_first_name(self, data):
        """
        Check that the start is before the stop.
        """
        nv=0
        val= self.initial_data['last_name']
        for i in val:
            raise serializers.ValidationError(val)

        for i in data:
            raise serializers.ValidationError(data)
            if i in 'adiouAEIOU':
                nv = nv + 1
                if nv > 0:
                    validate_last_name()
                    raise serializers.ValidationError('error, vowel in first name')


        return data



