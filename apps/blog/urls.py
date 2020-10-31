from django.urls import path
from apps.blog import views


urlpatterns = [
    path('', views.BlogIndex.as_view(), name="index_blog"),
]
