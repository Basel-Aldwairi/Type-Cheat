import threading
import queue

# Shared queue between threads
q = queue.Queue()

def input_thread():
    while True:
        user_input = input("Type something: ")
        q.put(user_input)   # put input into queue
        if user_input.lower() == "exit":
            break

def worker_thread():
    while True:
        msg = q.get()       # wait until something is in the queue
        if msg.lower() == "exit":
            print("Worker stopping.")
            break
        print(f"Worker received: {msg}")

# Start threads
t1 = threading.Thread(target=input_thread)
t2 = threading.Thread(target=worker_thread)

t1.start()
t2.start()

t1.join()
t2.join()
