from django.shortcuts import render, get_object_or_404

# Импортируем модель, чтобы обратиться к ней
from .models import Post, Group


def index(request):
    """В переменную posts будет сохранена выборка из 10 объектов модели Post,
    отсортированных по полю pub_date по убыванию
    (от больших значений к меньшим).
    """
    posts = Post.objects.order_by("-pub_date")[:10]
    # В словаре context отправляем информацию в шаблон
    context = {
        "posts": posts,
    }
    return render(request, "posts/index.html", context)


def group_posts(request, slug):
    """Страница список постов."""
    group = get_object_or_404(Group, slug=slug)

    # Метод .filter позволяет ограничить поиск по критериям.
    posts = Post.objects.filter(group=group).order_by("-pub_date")[:10]

    template = "posts/group_list.html"
    context = {
        "group": group,
        "posts": posts,
    }
    return render(request, template, context)
