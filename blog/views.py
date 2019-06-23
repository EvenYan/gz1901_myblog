from django.db.models import Count
from django.shortcuts import render, get_object_or_404

# Create your views here.
from blog.models import Post, Category


def index(request):
    post_list = Post.objects.all()

    recent_post = Post.objects.all().order_by("-created_time")[:5].values("title", 'id')
    archive = Post.objects.dates('created_time', 'month', order='ASC')
    category_list = Category.objects.annotate(post_num=Count("post")).filter(post_num__gt=0)
    print(category_list[0].name)
    print(category_list[0].post_num)
    context = {"post_list": post_list, "recent_post": recent_post, "archive": archive, "category_list": category_list}
    return render(request, 'blog/index.html', context=context)


def detail(request, id):
    post = Post.objects.filter(id=id)[0]
    context = {"post": post}
    return render(request, 'blog/detail.html', context)


def archive(request, year, month):
    post_list = Post.objects.filter(created_time__year=year, created_time__month=month)
    context = {"post_list": post_list}
    return render(request, 'blog/index.html', context)


def category(request, id):
    print(id)
    cate = get_object_or_404(Category, pk=id)
    print(cate)
    post_list = Post.objects.filter(category=cate)
    context = {"post_list": post_list}
    return render(request, 'blog/index.html', context)