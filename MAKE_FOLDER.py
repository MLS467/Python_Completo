from dataclasses import dataclass
import os
import pathlib
import re

"""
aula000/
├── meu_teste.py
├── rascunho.py
├── notes.md
├── modules/
│   ├── __init__.py
│   └── utils.py
├── data/
│   └── exemplo.json
└── tests/
    └── test_meu_teste.py
"""


# Class para criar uma nova pasta com estrutura padrão
@dataclass
class MakeFolder:
    name_folder: str  # Nome da pasta principal (ex: aula001)
    name_file: str  # Nome do arquivo principal da aula
    path_temp: bool  # Criar rascunho.py?
    with_modules: bool  # Criar pasta modules?
    with_data: bool  # Criar pasta data?
    with_notes: bool  # Criar notes.md?
    with_tests: bool  # Criar pasta tests?


# Função para criar estrutura completa da aula
def new_folder_class(make_folder: MakeFolder) -> None:
    new_name_file = re.sub(
        r"[-\s]+", "_", make_folder.name_file.strip().lower()
    )

    # Caminhos principais
    PATH_ROOT = pathlib.Path(__file__).parent / make_folder.name_folder
    PATH_NEW_FILE = PATH_ROOT / f"{new_name_file}.py"
    PATH_TEMP = PATH_ROOT / "rascunho.py"

    PATH_ROOT.mkdir(exist_ok=True)

    # Arquivos principais
    PATH_NEW_FILE.touch(exist_ok=True)
    if make_folder.path_temp:
        PATH_TEMP.touch(exist_ok=True)

    # Estrutura opcional
    if make_folder.with_modules:
        modules_path = PATH_ROOT / "modules"
        modules_path.mkdir(exist_ok=True)
        (modules_path / "__init__.py").touch()
        (modules_path / "utils.py").touch()

    if make_folder.with_data:
        data_path = PATH_ROOT / "data"
        data_path_img = data_path / "img"
        data_path.mkdir(exist_ok=True)
        data_path_img.mkdir(exist_ok=True)
        (data_path / "exemplo.json").touch()

    if make_folder.with_notes:
        (PATH_ROOT / "notes.md").touch()

    if make_folder.with_tests:
        tests_path = PATH_ROOT / "tests"
        tests_path.mkdir(exist_ok=True)
        (tests_path / f"test_{new_name_file}.py").touch()


# Interação com o usuário
def get_data_folder() -> None:
    os.system("cls" if os.name == "nt" else "clear")

    print("=== Criador de Estrutura de Aula ===")
    name_file = input("Digite o nome do arquivo principal da aula: ").strip()
    folder_name = input("Digite o nome da pasta: ").strip()
    path_temp = input("Criar rascunho.py? (S/N): ").strip().lower() == "s"
    with_modules = (
        input("Criar pasta de módulos (modules/)? (S/N): ").strip().lower()
        == "s"
    )
    with_data = (
        input("Criar pasta de dados (data/)? (S/N): ").strip().lower() == "s"
    )
    with_notes = (
        input("Criar arquivo de notas (notes.md)? (S/N): ").strip().lower()
        == "s"
    )
    with_tests = (
        input("Criar pasta de testes (tests/)? (S/N): ").strip().lower() == "s"
    )

    folder = MakeFolder(
        name_folder=folder_name,
        name_file=name_file,
        path_temp=path_temp,
        with_modules=with_modules,
        with_data=with_data,
        with_notes=with_notes,
        with_tests=with_tests,
    )

    new_folder_class(folder)
    print(f"\n✅ Estrutura criada em: {folder_name}/")


if __name__ == "__main__":
    get_data_folder()
