from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from news.models import News, Category
from news.filters import NewsFilter


def main(request):
    news = News.objects.all().order_by('-date', 'name')

    search = request.GET.get('search')
    if search:
        news = news.filter(name__icontains=search)

    filter_set = NewsFilter(request.GET, queryset=news)

    paginator = Paginator(filter_set.qs, 8)
    page = int(request.GET.get('page', 1))
    news = paginator.get_page(page)

    return render(request, 'index.html', {'news': news, 'filter': filter_set})


def detail_news(request, id):
    # try:
    #     news = News.objects.get(id=id)
    # except News.DoesNotExist:
    #     raise Http404()

    news = get_object_or_404(News, id=id)

    return render(request, 'detail_news.html', {'news': news})


def news_by_category(request, id):
    category = get_object_or_404(Category, id=id)
    news = News.objects.filter(category=category).order_by('-date', 'name')

    paginator = Paginator(news, 8)
    page = int(request.GET.get('page', 1))
    news = paginator.get_page(page)

    return render(request, 'index.html', {'news': news, 'category': category})



# Create your views here.
