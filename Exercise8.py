"""8. Write a function in Python that implements the following algorithm.
The sieve of Eratosthenes is a simple algorithm for finding all prime numbers up to a specified
integer. The algorithm to find all the prime numbers less than or equal to a given integer n:
1) Create a list of integers from two to n: 2, 3, 4, ..., n
2) Start with a counter i set to 2, i.e. the first prime number
3) Starting from i+i, count up by i and remove those numbers from the list, i.e. 2i, 3i, 4*i,
etc..
4) Find the first number of the list following i. This is the next prime number.
5) Set i to the number found in the previous step
6) Repeat steps 3 and 4 until i is greater than n. (As an improvement: It's enough to go to
the square root of n)
All the numbers, which are still in the list, are prime numbers
HINT: You can easily see that we would be inefficient, if we strictly used this algorithm, e.g. we
will try to remove the multiples of 4, although they have been already removed by the multiples
of 2. So it's enough to produce the multiples of all the prime numbers up to the square root of n.
"""
# condition first
n= int(input("Enter the number: "))
numbers =[_ for _ in range (2,n+1)]
primes =[]

while numbers:
    condition=numbers[0]
    primes.append(condition)
    for i in range(condition,n+1,condition):
        if i in numbers:numbers.remove(i)
print(primes)

# Condition second

lower = int(input("Enter the lower number:"))
upper = int(input("Enter the upper number: "))
print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower,upper + 1):
    #all the prime numbers are greater than 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
            else:
                print(num)

# Condition 4

def nextprime(n):
    p=n+1
    for i in range(2,p):
        if (p%i == 0):
            p=p+1
    else:
        print(p,end="")
n=int(input("Enter value to find next prime number:"))
nextprime(n)
print(" is the next prime number")


