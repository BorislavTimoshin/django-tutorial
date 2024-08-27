from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render

from .models import Category, TagPost, Women

menu = [
    {
        'title': 'О сайте',
        'url_name': 'about',
    },
    {
        'title': 'Добавить статью',
        'url_name': 'add_page',
    },
    {
        'title': 'Обратная связь',
        'url_name': 'contact',
    },
    {
        'title': 'Войти',
        'url_name': 'login',
    },
]


def index(request: HttpRequest) -> HttpResponse:
    posts = Women.published.all().select_related('cat')
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': posts,
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', context=data)


def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'women/about.html', {'title': 'О сайте', 'menu': menu})


def show_post(request: HttpRequest, post_slug: int) -> HttpResponse:
    post = get_object_or_404(Women, slug=post_slug)
    data = {
        'title': post.title,
        'menu': menu,
        'post': post,
        'cat_selected': 1,
    }
    return render(request, 'women/post.html', context=data)


def show_category(request: HttpRequest, cat_slug: int) -> HttpResponse:
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Women.published.filter(cat_id=category.pk).select_related('cat')

    data = {
        'title': f'Рубрика {category.name}',
        'menu': menu,
        'posts': posts,
        'cat_selected': category.pk,
    }
    return render(request, 'women/index.html', context=data)


def page_not_found(request: HttpRequest, exception: Exception) -> HttpResponseNotFound:
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def addpage(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Добавление статьи')


def contact(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Обратная связь')


def login(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Авторизация')


def show_tag_postlist(request: HttpRequest, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)
    posts = tag.posts.filter(is_published=Women.Status.PUBLISHED).select_related('cat')

    data = {
        'title': f'Тег: {tag.tag}',
        'menu': menu,
        'posts': posts,
        'cat_selected': None,
    }

    return render(request, 'women/index.html', context=data)
