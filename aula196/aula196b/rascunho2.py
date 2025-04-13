import threading
from time import sleep


def vai_demorar(text: str, tempo: int) -> None:
    sleep(tempo)
    print(text)


valor_variado = 10
params = {"target": vai_demorar, "args": ("THREAD 1 EXECUTOU", valor_variado)}
T1 = threading.Thread(**params)
T1.start()

for i in range(20):
    print("Executando espere...")
    if T1.is_alive():
        continue
    break
