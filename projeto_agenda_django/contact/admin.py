from django.contrib import admin
from contact.models import Contact

# Register your models here.


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "phone",
        "email",
        "description",
        "created_date",
    )

    # filtra os dados na área admin
    # list_filter = ("created_date",)

    # adiciona um campo de pesquisa pela coluna desejada
    search_fields = ("id",)

    # ordena em modo descrecente (-), creceste é padrão
    ordering = ("-id",)

    # faz uma listagem de (n) contatos para não carregar muitos de uma vez só
    list_per_page = 10

    # limita a listagem em 100 registros
    list_max_show_all = 100

    # adiciona um campo editável na listagem
    list_editable = (
        "last_name",
        "email",
    )

    # adiciona um link para editar o contato na listagem
    # mas não pode ser editável com list_editable
    list_display_links = ("id", "first_name")
