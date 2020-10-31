from rest_framework import serializers
from apps.blog import models


class PostSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    def get_username(self, obj):
        return obj.user.username

    class Meta:
        model = models.Post
        fields = '__all__'
