"""
A function to generate Fibonacci sequence from 0  to n
"""

def fib_recursive(x):  # recursive function, meaning the function can call itself
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fib_recursive(x-1) + fib_recursive(x-2)    

n = int(input("Please enter value: "))    # n is the number of terms
if n <= 0:
    print ("Only positive numbers please")
else:
    for i in range(n):
        print(fib_recursive(i))            
