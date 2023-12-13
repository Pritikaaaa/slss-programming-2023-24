# Functions and Recursions
# Author: Pritika Vats
# December 06, 2023

import time

def factorial(num: int) -> int:
    """Returns the result of the numbe's 
    factorial using recursion
    
    Params:
        num - number we're calculating
        
    Returns:
        result
    """
    if num == 0 or num == 1:
        return 1
    elif num > 1:
        return factorial(num - 1) * num
    
def fib(n: int) -> int:
    """calculate and return the nth
    Fibonacci number."""

    if n in [1,2]:
        return 1
    elif n > 2:
        return fib(n - 1) + fib(n - 2)
    
print(fib(1), fib(2), fib(8))

    
print(factorial(1))


def fib_itr(n: int) -> int:
    """Returns the nth fibonacci number.
    Calculates this iteratively."""
    last_num, num, result = 0,1,0

    for _ in range(n):
        result = last_num + num

        num, last_num = result, num

    return result

time_initial = time.perf_counter()
fib_itr(10)
time_final = time.perf_counter()

print(fib)












  