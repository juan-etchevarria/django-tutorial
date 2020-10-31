from django.urls import include, path
from apps.blog import views
from apps.blog.api.urls import router


urlpatterns = [
    path('', views.BlogIndex.as_view(), name="index_blog"),
    path('post/<int:post_id>', views.PostIndex.as_view(), name="post_blog"),
    path('api/', include(router.urls)),
]
