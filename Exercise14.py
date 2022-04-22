'''  Write two generator function:
    a. The first, given N as input generates all the Fibonacci numbers up to N
    b. The second, given a list of numbers generates the corresponding list of elementwise
    pow2 numbers (e.g. given a sequence 1,2,3,… returns 1,4,9…)
    Use the two generator functions just built to evaluate the sum of the squares of the first N
    Fibonacci numbers and test it with N=10 '''

import itertools

def fibonacci(N):
    a , b = 0 ,1
    for i in range(N):
        yield a
        a,b = b,a+b
Fn=int(input(" How many number: "))
print("your fibonacci sequence is ")
result=list(itertools.islice(fibonacci(Fn),Fn))
print(result)

#Second Condition

def square():
    squares = lambda i : i*i
    print("squaring the numbers: ")
    print(list(map(squares,result)))
result2 = square()


# Calculating sum of square of fibanacci sequence
def calculateSquareSum(n):
    fibo = [0] * (n + 1);
    if (n <= 0):
        return 0;
    fibo[0] = 0;
    fibo[1] = 1;

    # Initialize result
    sum = ((fibo[0] * fibo[0]) +
           (fibo[1] * fibo[1]));

    # Add remaining terms
    for i in range(2, n + 1):
        fibo[i] = (fibo[i - 1] +
                   fibo[i - 2]);
        sum += (fibo[i] * fibo[i]);

    return sum;


# Driver Code
n = 10;

print("Sum of squares of Fibonacci numbers is :",
      calculateSquareSum(n));

