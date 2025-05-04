from tabnanny import verbose
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


class Category(models.Model):

    # Meta é uma classe interna que define opções adicionais para o modelo
    # verbose_name é o nome do modelo no singular
    # verbose_name_plural é o nome do modelo no plural
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name}"


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=255)
    created_date = models.DateField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    # picture é um campo de imagem,
    # o upload_to é o caminho onde a imagem será salva
    picture = models.ImageField(blank=True, upload_to="pictures/%Y/%m/")
    # category é uma chave estrangeira para a tabela Category,
    # o on_delete=models.SET_NULL significa que se a categoria for deletada,
    # o campo category do contato será setado como null
    category = models.ForeignKey(
        Category, blank=True, on_delete=models.SET_NULL, null=True
    )

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
