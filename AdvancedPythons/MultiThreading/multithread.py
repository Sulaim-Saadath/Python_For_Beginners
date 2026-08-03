import time
import threading
def print_numbers():
    print(f"Hello from {threading.current_thread().name}!")
    for i in range(1, 6):
        print(f"Number is {i}")
        time.sleep(1)
def print_letter():
    print(f"Hello from {threading.current_thread().name}!")
    for l in ['a', 'b', 'c', 'd', 'e']:
        print(f"Letters is {l}")
        time.sleep(1)
# Create threads
t1 = threading.Thread(target=print_numbers, name="thread1")
t2 = threading.Thread(target=print_letter, name="thread2")

t1.start()
t2.start()

t1.join() 
t2.join()

print("All tasks are completed.")
print(f"Is the thread 1 is Alive: {t1.is_alive()}.")