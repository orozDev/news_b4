from django.shortcuts import render, get_object_or_404
from django.http import Http404

from news.models import News


def main(request):
    news = News.objects.all()
    return render(request, 'index.html', {'news': news})


def detail_news(request, id):
    # try:
    #     news = News.objects.get(id=id)
    # except News.DoesNotExist:
    #     raise Http404()

    news = get_object_or_404(News, id=id)
    return render(request, 'detail_news.html', {'news': news})

# Cxreate your views here.
