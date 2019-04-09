import threading
import time

class myThread (threading.Thread):
    def __init__(self,threadName,counter):
        threading.Thread.__init__(self)
        self.name = threadName
        self.counter = counter

    def run(self):
        while self.counter >= 1:
            print("Starting %s - counter : %d "%(self.name, self.counter))
            self.counter -= 1
            time.sleep(1)
        print("Exiting %s"%(self.name))

# Create new threads
thread1 = myThread("Thread-1", 5)
thread2 = myThread("Thread-2", 4)

# Start new Threads
thread1.start()
thread2.start()
print("Exiting Main Thread")