"forks child processes until you type 'q'"
import os

def child():
    print('Hello from child', os.getpid())
    os._exit(0) # else goes back to parent loop

def parent():
    while True:
        newpid = os.fork()
        # newpid = 0 , we are in child process
        # newpid = positive value, we are in parent process
        # newpid = negative value, error occured
        if newpid == 0:
            child()
        else:
            print('Hello from parent', os.getpid(), newpid)
        if input() == 'q':
            break
            
parent()

# watch -n1 pgrep -l python
# ps axf | grep python