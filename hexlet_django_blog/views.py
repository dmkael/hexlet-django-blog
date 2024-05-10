from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView


# def index(request):
#     return render(request, 'index.html', context={
#         'who': 'World',
#     })

class MainView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'World'
        return context

    def get(self, request, *args, **kwargs):
        return redirect(reverse_lazy('article', kwargs={'id': 4}))


def about(request):
    tags = ['обучение', 'программирование', 'python', 'oop']
    return render(
        request,
        'about.html',
        context={'tags': tags},
    )
