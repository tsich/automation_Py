import threading
import time

def print_number():
    global number
    # print("Thread:", threading.get_ident(), "Number:", number)
    while number < 10:
        print("Number:", number)
        number += 1
        time.sleep(3)

number = 0
threads = []
for i in range(5):
    thread = threading.Thread(target=print_number)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()