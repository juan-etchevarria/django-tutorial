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
            .select_related('user')

        return context
