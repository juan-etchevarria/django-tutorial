from django.views.generic import TemplateView
from apps.blog.models import Post


class BlogIndex(TemplateView):
    """
    Index view
    """

    template_name = "blog/index.html"

    def get_context_data(self, **kwargs):
        context = super(BlogIndex, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(publish=True) \
            .select_related('user').order_by('-created')

        return context


class PostIndex(TemplateView):
    """
    Post view
    """

    template_name = "blog/post.html"

    def get_context_data(self, **kwargs):
        context = super(PostIndex, self).get_context_data(**kwargs)
        context['post_id'] = kwargs['post_id']

        return context
