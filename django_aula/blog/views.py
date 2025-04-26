from django.shortcuts import render

# from base.data import posts
import requests


# Create your views here.


def blog(request):
    try:
        URL = "https://jsonplaceholder.typicode.com/posts"
        result_request = requests.get(URL)
        result = result_request.json()
        msg = "dados carregados com sucesso!"
    except requests.exceptions.RequestException as e:
        msg = f"Erro ao carregar os dados {e}"
        result = None

    context_blog = {
        "name": "HOME BLOG",
        "title_aba": "Blog",
        "title": "Blog",
        "content": "Welcome to the blog page!",
        "posts": result,
        "msg": msg,
    }
    return render(request, "blog/home.html", context=context_blog)


def exemple(request):
    context_example = {
        "title_aba": "Example",
        "title": "Example",
        "content": "Welcome to the Example page!",
    }
    return render(request, "blog/exemple.html", context=context_example)
