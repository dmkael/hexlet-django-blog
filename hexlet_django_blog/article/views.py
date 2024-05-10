from hexlet_django_blog.views import MainView
from django.shortcuts import render, get_object_or_404, redirect
from hexlet_django_blog.article.models import Article
from django.contrib import messages
from .forms import ArticleForm


# Create your views here.
class ArticleListView(MainView):
    template_name = 'article/index.html'

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        return render(request, self.template_name, context={'articles': articles})


class ArticleView(MainView):
    template_name = 'article/article.html'

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, self.template_name, context={'article': article})


class ArticleFormCreateView(MainView):

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'article/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():  # Если данные корректные, то сохраняем данные формы
            form.save()
            messages.add_message(request, messages.INFO, 'Article created.')
            return redirect('articles')  # Редирект на указанный маршрут
        # Если данные некорректные, то возвращаем человека обратно на страницу с заполненной формой
        return render(request, 'articles/create.html', {'form': form})


# def index(request):
#     return render(request, 'article/index1.html', context={'name': 'article'})
