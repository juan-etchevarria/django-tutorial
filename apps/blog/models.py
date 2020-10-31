import os

from django.db import models
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string


class Post(models.Model):
    """
    Model Post

    """

    def generate_path_blog_image(instance, filename):
        """
        Generate path to field photo
        """
        return os.path.join(
            "posts", "post_" + instance.image_id, filename
        )

    title = models.CharField("Title", max_length=150, blank=False, null=False)
    description = models.TextField('Description', blank=False, null=False)
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(
        'Created', blank=False, auto_now_add=True, db_index=False
    )
    updated = models.DateTimeField(
        'updated', blank=False, auto_now=True, db_index=False
    )
    user = models.ForeignKey(
        get_user_model(), related_name='post_users',
        on_delete=models.CASCADE, null=True, blank=True
    )
    image_id = models.CharField(
        max_length=200, null=True, blank=True, editable=False
    )
    image = models.FileField(
        "Image", upload_to=generate_path_blog_image,
        null=True, blank=True,
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.generate_image_id(self.image_id)
        super(Post, self).save(*args, **kwargs)

    def generate_image_id(self, value):
        """
        Generate id for photo files
        """

        if not value:
            self.image_id = get_random_string(length=32)
