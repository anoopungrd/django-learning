# from django.shortcuts import render
# from .models import Post
from django.views.generic import ListView  # Added for using ListView
from .models import Post


# def post_list(request):
#     posts = Post.objects.all()
#     return render(request, "post_list.html", {"posts": posts})


class PostList(ListView):  # Using ListView instead of function based view as above
    model = Post
    template_name = "post_list.html"
