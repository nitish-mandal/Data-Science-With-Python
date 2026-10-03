## Multiprocessing means using multiple CPU cores at the same time to complete heavy work faster.
## When a task requires a lot of calculation (like finding the factorial of a very large number), we divide the 
# work into parts and give each part to a different CPU core.
## Because the work happens at the same time (in parallel), the task finishes faster.

import multiprocessing
import math
import sys
import time

## Increase the maximun number of digits for integer conversion 
sys.set_int_max_str_digits(100000)

## function to compute factorials of a given numbers 

def computer_factorial(number):
    print(f"Computing factorial of {number}")
    result=math.factorial(number)
    print(f"Factorial of {number} is {result}")
    return result

if __name__=="__main__":
    numbers=[5000,3000,2000,7000]

    start_time=time.time()

    ## create a pool of worker

    with multiprocessing.Pool() as pool:
        results=pool.map(computer_factorial,numbers)

    end_time= time.time()

    print(f"Results: {results}")
    print(f"Time taken: {end_time - start_time} seconds")