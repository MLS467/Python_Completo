"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin

# importando o arquivo urls.py do app contact
from contact import urls as contact_urls

# importando a função include e path do django.urls
from django.urls import include, path

# importando a função static do django.conf.urls.static
from django.conf.urls.static import static

# importando o settings do django.conf
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(contact_urls)),
]

# adicionando o static ao urlpatterns
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
