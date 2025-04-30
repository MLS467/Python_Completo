from django.utils import timezone
from django.db import models


# Create your models here.

# id (primary key - automatico não preocupa)
# first_name(string) string campo de texto limitado a 255 caracteres
# last_name(string)
# phone(string)
# email(string)
# created_at(datetime) data de criação do contato
# description(text)
# category (foreign key) categoria do contato
# show (boolean) se o contato deve ser exibido ou não
# owner (foreign key) usuário dono do contato
# picture (image) imagem do contato


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=255)
    created_date = models.DateField(default=timezone.now)
    description = models.TextField(blank=True)
