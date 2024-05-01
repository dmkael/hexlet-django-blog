from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'article/index1.html', context={'name': 'article'})
