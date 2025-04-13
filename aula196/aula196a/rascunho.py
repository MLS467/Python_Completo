import time
from Thread1 import My_Thread


print("Hello World")


t1 = My_Thread("Thread 1", 7)
t2 = My_Thread("Thread 2", 5)

t1.start()
t2.start()

for i in range(10):
    print(i)
    time.sleep(1)

print("End of the program")
