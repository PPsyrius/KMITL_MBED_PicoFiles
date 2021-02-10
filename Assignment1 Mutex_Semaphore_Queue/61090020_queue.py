# Assignment 1.2: Queue Implementation for Python 3.9

import threading, queue

SIZE = 10

q1 = queue.Queue()      # First In, First Out
q2 = queue.LifoQueue()  # Last in, First Out a.k.a. Stack

for i in range(SIZE):   # All are inserted from 1 to SIZE
    q1.put(i)
    q2.put(i)
    
def Queue(q, queuetype):
    global SIZE
    for i in range(SIZE):
        print("{}: {}".format(queuetype, q.get()))
        
t1 = threading.Thread(target = Queue(q1,"FIFO"))
t2 = threading.Thread(target = Queue(q2,"LIFO/Stack"))

t1.start()
t2.start()
