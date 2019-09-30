from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, postid):
    post = get_object_or_404(Post, pk=postid)
    print(postid)
    print(post)
    print(post.title)
    return render(request, 'blog/post_detail.html', {'post': post})
