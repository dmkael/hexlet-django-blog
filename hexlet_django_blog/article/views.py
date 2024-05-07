from hexlet_django_blog.views import MainView
from django.shortcuts import render
from hexlet_django_blog.article.models import Article


# Create your views here.
class ArticleListView(MainView):
    template_name = 'article/index.html'

    def get(self,request, *args, **kwargs):
        articles = Article.objects.all()
        return render(request, self.template_name, context={'articles': articles})


class ArticleView(MainView):
    template_name = 'article/article.html'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        article = Article.objects.get(pk=context.get('article_id'))
        context.update({"article": article})
        return render(request, self.template_name, context=context)

# def index(request):
#     return render(request, 'article/index1.html', context={'name': 'article'})
