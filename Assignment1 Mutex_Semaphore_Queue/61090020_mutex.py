# Assignment 1.1: Mutual Exclusion Object (Mutex) Implementation for Python 3.9

import threading, time

# gloval variable
data = 0
mutex = threading.Lock() # Is a locking mechanism

def producer():
    print("\n#-- Producer Created --#")
    for produced in range(5):
        mutex.acquire()
        global data
        data += 1
        mutex.release()
        print("Produced: {}".format(data))


### Main Goes Here ###
print("\n#-- Main Init --#")

# Creating Thread
pro1 = threading.Thread(target=producer)
pro2 = threading.Thread(target=producer)

# Start Thread
pro1.start()
pro2.start()

# Join Thread
pro1.join()
pro2.join()

print("#-- Main Done --#")

