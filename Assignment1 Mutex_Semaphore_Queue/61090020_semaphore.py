# Assignment 1.3: Semaphore Implementation for Python 3.9
# As this is Binary Semaphore, the result should be similar to Mutex

import threading, time

# gloval variable
data = 0
sem = threading.Semaphore() # Is just a signaling mechanism

def producer():
    print("\n#-- Producer Created --#")
    for produced in range(5):
        sem.acquire()
        global data
        data += 1
        sem.release()
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
