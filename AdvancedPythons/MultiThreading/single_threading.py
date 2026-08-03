import time
def print_numbers():
    for i in range(1, 6):
        print(f"Number is {i}")
        time.sleep(0.5)
def print_letter():
    for l in ['a', 'b', 'c', 'd', 'e']:
        print(f"Letters is {l}")
        time.sleep(0.5)
print_numbers()
print_letter()