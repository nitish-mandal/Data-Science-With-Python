### Multithreading
## When to use multithreading
## I/O- bound tasks: Tasks that spend more time waiting for I/O operations (e.g., file operations , network requests).
## Concurrent execution : when youn want to improve the throughput od your application  by performing multiple operations concurrently 


import threading 
import time

def print_number():
    for i in range(5):
        time.sleep(2)
        print(f"Number : {i}")

def print_letters():
    for letter in "abcd":
        time.sleep(5)
        print(f"Letter : {letter}")

## create 2 thread
t1= threading.Thread(target= print_number)
t2 = threading.Thread(target= print_letters)

t= time.time()
# start thr thread
t1.start()
t2.start()  

## wait for the threads to complete 
t1.join()
t2.join()
finished_time=time.time()-t
print(finished_time)     
