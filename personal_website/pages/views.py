from django.shortcuts import render
from django.http import HttpResponse


def home_page_view(request):
    return HttpResponse("HomePage")


def about_page_view(request):
    context = {"name": "Anoop", "age": 41}
    return render(request, "pages/about.html", context)


# Create your views here.
