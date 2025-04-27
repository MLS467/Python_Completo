from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("post/", views.blog, name="blog"),
    path("post/<int:post_id>", views.post, name="post"),
    path("exemple/", views.exemple, name="exemple"),
]
