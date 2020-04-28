from django.contrib.auth.models import User, Group
from rest_framework import serializers

from core.models import Post, Nangareko


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'cic',
            'fullname',
            'social_code'
        )


class NangarekoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nangareko
        fields = [
            'cic',
            'fullname',
            'phone',
            'carrier',
            'observation',
            'payment_confirmed',
            'sent_sms',
            'received_sms',
            'requested'
        ]
