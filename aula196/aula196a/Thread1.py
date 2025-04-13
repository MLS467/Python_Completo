from threading import Thread
from time import sleep


class My_Thread(Thread):
    def __init__(self, name: str, time_: int) -> None:
        super().__init__()
        self.name = name
        self.time_ = time_

    def run(self) -> None:
        sleep(self.time_)
        print(f"{self.name} finished sleeping for {self.time_} seconds")
