import sys
from threading import Thread
import random
import time
from pynput import keyboard
flag = 1
flag1 =1
que= []
for i in range(200):
    que.append(random.randint(1, 100))

def consumer(m):
    while flag == 1:
        time.sleep(1)
        if len(que) > 0:
            a = que[0]
            que.remove(a)
            print(que, '\n', len(que), '\n')
        else:
            break
    if flag==0:
        while len(que)>0:
            a = que[0]
            que.remove(a)
            print(que, '\n', len(que), '\n')


def produce(n):
    while flag == 1:
        time.sleep(1)
        if len(que) <= 80:
            a = random.randint(1, 100)
            que.append(a)
            print(que, '\n', len(que), '\n')
        elif len(que) >= 100:
            time.sleep(1)
    if flag == 0:
        exit()



def on_release(key):
    global flag
    print(f'{key} released')
    if key == keyboard.KeyCode(char='q'):
        flag = 0



thread1 = Thread(target=consumer, args=(1,))
thread1.start()
thread2 = Thread(target=consumer, args=(2,))
thread2.start()
thread3 = Thread(target=produce, args=(1,))
thread3.start()
thread4 = Thread(target=produce, args=(2,))
thread4.start()
thread5 = Thread(target=produce, args=(3,))
thread5.start()

with keyboard.Listener(
        on_release=on_release) as listener:
    listener.join()
