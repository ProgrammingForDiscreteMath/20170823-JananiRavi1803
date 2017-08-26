		""" Python course: Assignment-2
    			Date : 24/08/2017 """

### (1) Print numbers from the list less than 10

def entries_less_than_ten(L):
    """
    Return elements of the list less than 10
    """
    M = [i for i in L if i<10]
    return M

		####OUTPUT####

entries_less_than_ten(range(-15, 50, 5))
#[-15, -10, -5, 0, 5]


### (2) Print negative numbers from the list
def number_of_negatives(L):
    """
    Return the number of negative numbers in L.
    """
    M = [i for i in L if i<0]
    l = len(M)
    return l

		####OUTPUT####
number_of_negatives(range(-15, 50, 5))
#3


### (3) Print common elements from two different lists
def common_elements(L1, L2):
    """
    Return the common elements of lists ``L1`` and ``L2`` 	  without duplicates
    """
    C= [i for i in L1 if i in L2]
    return C

common_elements(range(-30,30,5), range(-20,20,3))

#[-20, -5, 10]


### (4) Fibonacci sequence generator function
def fibonacci_generator():
    """
    Generate the Fibonacci sequence 1, 1, 2, 3, 5, 8, 13, 21,...
    """
    a1, a2 = 1, 1
    while True:
        yield a1
        a1, a2 = a2, a1+a2

f= fibonacci_generator()
[f.next() for i in range(10)]

		####OUTPUT####

#[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


### (5) Largest fibonacci number before the value 'n'
def largest_fibonacci_before(n):
    """
    Return the largest Fibonacci number less than ``n``.
    """
    f = fibonacci_generator()
    l = []
    while True:
        x= f.next()
        l.append(x)
        #print x
        if x >= n:
            break
    return l[-2]

		####OUTPUT####

largest_fibonacci_before(13)
#8
largest_fibonacci_before(200)
#144


### (6) Catalan sequence generator function
def catalan_generator():
    """
    Generate the sequence of Catalan numbers.
    """
    a1, a2 = 0,1
    while True:
        yield a2
        a1 = a1+1 
        a2 = a2 * 2 * (2*a1-1) / (a1+1) 

c = catalan_generator()
[c.next() for i in range(10)]

		####OUTPUT####
#[1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862]


### (7) Find the factorial value of 'n'
def factorial(n):
    """
    The function returns the factorial value of n
    """
    if n==0:
        return 1
    elif n>=1:
        fact = 1
        for i in range(1, n+1):
            fact = fact*i
        return fact

		####OUTPUT####
factorial(5)
#120
factorial(10)
#3628800

