import threading
from time import sleep


def vai_demorar(text: str, tempo: int) -> None:
    sleep(tempo)
    print(text)


# valor_variado = random.randint(1, 10)
valor_variado = 5
params = {"target": vai_demorar, "args": ("THREAD 1 EXECUTOU", valor_variado)}
T1 = threading.Thread(**params)
T1.start()


for i in range(20):
    vai_demorar(f"Contando {i}", 1)
    print("Contando...")
    sleep(1)
