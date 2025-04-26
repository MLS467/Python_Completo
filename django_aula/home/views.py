from django.shortcuts import render


# Create your views here.
def home(request):
    contexto = {
        "title_aba": "Home",
        "title_text": "Home",
        "description_text": "Essa é a página inicial do site",
    }

    return render(request, "home/home.html", contexto)
