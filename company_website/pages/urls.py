from django.urls import path
from .views import home_page_view, AboutPageView

urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),  # named URL
    path("", home_page_view, name="home"),  # named URL
]
