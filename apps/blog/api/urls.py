from rest_framework import routers
from apps.blog.api import views


# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet)
