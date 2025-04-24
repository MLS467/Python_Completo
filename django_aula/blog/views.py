from django.http import HttpResponse

# from django.shortcuts import render


# Create your views here.
def blog(request):
    return HttpResponse(
        """
        <h1>blog do App</h1>
        <a href='/'>Home</a>
        """
    )
