from typing import Any
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render
import requests

# Create your views here.


def blog(request: HttpRequest) -> HttpResponse:
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


def exemple(request: HttpRequest) -> HttpResponse:
    context_exemple = {
        "name": "EXEMPLE",
        "title": "Exemple",
        "content": "Welcome to the Exemple page!",
    }

    return render(request, "blog/exemple.html", context=context_exemple)


def post(request: HttpRequest, post_id: int) -> HttpResponse:
    try:
        URL = f"https://jsonplaceholder.typicode.com/posts/{post_id}"

        result_request = requests.get(URL)
        selected_post: Any = result_request.json()

        if not selected_post:
            raise Http404(f"Post with id {post_id} not found.")

    except Http404 as e:
        raise Http404(f"Post with id {post_id} not found. Error: {e}")
    except requests.exceptions.RequestException as e:
        raise Http404(f"Error fetching post with id {post_id}. Error: {e}")

    data_post: dict = {
        "title": "Post",
        "posts": [selected_post],
        "title_aba": selected_post["title"],
    }

    return render(request, "blog/home.html", context=data_post)
