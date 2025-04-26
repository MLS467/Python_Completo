import pathlib
import re
import datetime


def new_folder_class(make_folder: str) -> None:
    try:
        time_message = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_name_file = re.sub(
            r"[-\s]+",
            "_",
            make_folder.strip().lower().replace(",", ""),
        )

        PATH_ROOT = pathlib.Path(__file__).parent
        PATH_NEW_FILE = PATH_ROOT / "ordem_das_aulas_por_commit.txt"
        PATH_EXISTING = PATH_NEW_FILE.exists()

        if PATH_EXISTING:
            with open(PATH_NEW_FILE, "r", encoding="utf-8") as file:
                lines = len(file.readlines())
        else:
            lines = 1

        with open(PATH_NEW_FILE, "a+", encoding="utf-8") as file:
            file.write(f"aula_{lines} -> {new_name_file} {time_message}\n")
    except Exception as e:
        print(f"Erro ao criar o arquivo: {e}")


if __name__ == "__main__":
    make_folder = input("digite o nome da aula: ")

    new_folder_class(make_folder)
    print(f"Arquivo {make_folder} criado com sucesso!")
