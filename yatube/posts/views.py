from django.shortcuts import render, get_object_or_404

from .models import Post, Group

POST_PER_PAGE = 10

def index(request):
    """В переменную posts будет сохранена выборка из 10 объектов модели Post,
    отсортированных по полю pub_date по убыванию
    (от больших значений к меньшим).
    """
    posts = Post.objects.all()[:POST_PER_PAGE]
    context = {
        "posts": posts,
    }
    return render(request, "posts/index.html", context)


def group_posts(request, slug):
    """Страница список постов."""
    group = get_object_or_404(Group, slug=slug)

    posts = group.posts.all()[:POST_PER_PAGE]
    template = "posts/group_list.html"
    context = {
        "group": group,
        "posts": posts,
    }
    return render(request, template, context)
