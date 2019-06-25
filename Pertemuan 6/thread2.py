"spawn threads until you type 'q'"
import _thread
import time

def child(tid):
    time.sleep(3)
    print('Hello from thread', tid)

def parent():
    i = 0
    for x in range(10) :    
        i += 1
        # Dengan Thread
        _thread.start_new_thread(child, (i,))
        # Tanpa Thread
        # child(i)
        time.sleep(1)

parent()

# date; python3.7 thread2.py; date