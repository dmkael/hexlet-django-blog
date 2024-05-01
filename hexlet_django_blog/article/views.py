# from django.shortcuts import render
from hexlet_django_blog.views import View


# Create your views here.
class ArticleView(View):
    template_name = 'article/index1.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'article'
        return context

# def index(request):
#     return render(request, 'article/index1.html', context={'name': 'article'})
