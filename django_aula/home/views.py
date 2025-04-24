from django.http import HttpResponse

# from django.shortcuts import render


# Create your views here.
def home(request):
    return HttpResponse(
        """
        <h1> Home do App </h1>
        <a href='blog'>Blog</a>
        """
    )
