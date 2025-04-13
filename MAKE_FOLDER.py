from dataclasses import dataclass
import os
import pathlib


# Class para criar uma nova pasta e dois arquivos dentro dela
@dataclass
class MakeFolder:
    name_folder: str
    name_file: str
    path_temp: bool


# Função para criar uma nova pasta e dois arquivos dentro dela
def new_folder_class(make_folder: MakeFolder) -> None:
    new_name_file = make_folder.name_file.replace("-", " ").replace(" ", "_")
    PATH_ROOT = pathlib.Path(__file__).parent / make_folder.name_folder
    PATH_NEW_FOLDER = PATH_ROOT / f"{new_name_file}.py"
    PATH_TEMP = PATH_ROOT / "rascunho.py"
    PATH_ROOT.mkdir(exist_ok=True)

    if make_folder.path_temp:
        LIST_FILES = [PATH_NEW_FOLDER, PATH_TEMP]
        for file in LIST_FILES:
            file.touch(exist_ok=True)
    else:
        PATH_NEW_FOLDER.touch(exist_ok=True)


# Adiciona o conteúdo do arquivo rascunho.py ao novo arquivo
def get_data_folder() -> None:
    os.system("cls" if os.name == "nt" else "clear")

    NAME_CURRENT_FILE = input("Digite o nome do arquivo atual: ")
    FOLDER_ROOT = input("Digite o nome da pasta original: ")
    PATH_TEMP = input("Criar rascunho S/N: ").lower() == "s"
    dict_kwargs = MakeFolder(FOLDER_ROOT, NAME_CURRENT_FILE, PATH_TEMP)
    new_folder_class(dict_kwargs)


get_data_folder()
