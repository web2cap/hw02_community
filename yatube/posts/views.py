from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from .models import Post, Group, User

POST_PER_PAGE = 10


def index(request):
    """В переменную page_obj будет сохранена выборка из POST_PER_PAGE объектов модели Post,
    отсортированных по полю pub_date по убыванию,
    с учетом номера страницы переданного в GET.
    """

    post_list = Post.objects.all().order_by("-pub_date")
    paginator = Paginator(post_list, POST_PER_PAGE)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
    }
    return render(request, "posts/index.html", context)


def group_posts(request, slug):
    """Страница список постов."""
    group = get_object_or_404(Group, slug=slug)

    post_list = group.posts.all()
    paginator = Paginator(post_list, POST_PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    template = "posts/group_list.html"
    context = {
        "group": group,
        "page_obj": page_obj,
    }
    return render(request, template, context)


def profile(request, username):
    """Список постов пользователя, общее количество постов, инофрмация о пользователе."""

    author = get_object_or_404(User, username=username)

    post_list = author.posts.all()

    paginator = Paginator(post_list, POST_PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    template = "posts/profile.html"
    context = {
        "page_obj": page_obj,
        "posts_count": post_list.count(),
        "author": author,
    }

    return render(request, template, context)


def post_detail(request, post_id):
    """Страница поста и количество постов пользователя."""
    post = get_object_or_404(Post, pk=post_id)

    post_list = post.author.posts.all()

    template = "posts/post_detail.html"
    context = {
        "post": post,
        "posts_count": post_list.count(),
    }
    return render(request, template, context)
