import time
num = [1, 2, 3, 4] # Iterable

# for n in num:
#     print(n)
#     pass

# try:
#     it = iter(num) #Object
#     print(next(it))
#     print(next(it))
#     print(next(it))
#     print(next(it))
#     print(next(it))
# except StopIteration as e:
#     print("No more items")

import time

# Custom iterator class
class CounterUpto:

    # Constructor: Initializes the limit and current count
    def __init__(self, limit):
        self.limit = limit      # Maximum value to count up to
        self.current = 0        # Starting value
        print("Inside constructor")

    # Makes this object iterable
    def __iter__(self):
        print("Inside dunder iter")
        return self             # Return the iterator object itself

    # Returns the next value during iteration
    def __next__(self):
        print("Inside dunder next")

        # Pause for 1 second before returning the next value
        time.sleep(1)

        # Check if counting is still within the limit
        if self.current < self.limit:

            # Increase current value by 1
            self.current += 1

            # Return the next number
            return self.current

        # No more values left to return
        else:
            raise StopIteration


# Create an iterator object that counts up to 5
counter = CounterUpto(5)

# Iterate through the object
for number in counter:

    # Print each number returned by __next__()
    print(number)