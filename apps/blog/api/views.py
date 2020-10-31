from rest_framework import viewsets
from apps.blog import models
from apps.blog.api import serializers


class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all().select_related('user')
    serializer_class = serializers.PostSerializer
