import threading
import time
def background_task():
    while True:
        print("Background task is running...")
        time.sleep(1)
    pass
thead = threading.Thread(target=background_task)
thead.daemon = True
thead.start()

time.sleep(3)
print("Main program ends.")
