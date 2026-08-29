from django.urls import path

# from .views import post_list, post_detail
from .views import BlogListView, BlogDetailView, BlogCreateView,BlogUpdateView,BlogDeleteView  # new

urlpatterns = [
    # path("post/<int:pk>/", post_detail, name="post_detail"),
    # path("", post_list, name="home"),
    path("post/new/", BlogCreateView.as_view(), name="post_new"),  # new
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),  # new
    path("post/<int:pk>/edit/", BlogUpdateView.as_view(), name="post_edit"), # Added for UpdateView
    path("post/<int:pk>/delete/", BlogDeleteView.as_view(), name="post_delete"), # Added for DeleteView
    path("", BlogListView.as_view(), name="home"),  # new
]
