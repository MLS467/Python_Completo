from django.shortcuts import render


# Create your views here.
def blog(request):
    context_blog = {
        "title_aba": "Blog",
        "title": "Blog",
        "content": "Welcome to the blog page!",
    }
    return render(request, "blog/home.html", context=context_blog)


def exemple(request):
    context_example = {
        "title_aba": "Example",
        "title": "Example",
        "content": "Welcome to the Example page!",
    }
    return render(request, "blog/exemple.html", context=context_example)
