import math

"""
 Fibonacci implementations with various algorithms.
 1) We have a naive solution when solving for the nth fibonacci number!
"""
def nthfibonacci(n):
    f1 = 0
    f2 = 1
    i = 0
    while i < n:
        temp = f1
        f1 = f2
        f2 = f2 + temp
        i +=1
    return f2

"""
2) Binets formula for the nth fibonacci number. No previous calculations have to be
done since the equation is of constant time. O(1). For larger n, using Binets formula
can lead to some inaccuracies due to rounding errors! Using phi (aka golden ratio)
which is an irrational number we can still manage to compute integers for all values
of n!
"""
def binetFibonacci(n):
    phi = (1+math.sqrt(5))/2
    return (phi**(n+1) - (1-phi)**(n+1))/math.sqrt(5)

n = 50
print('value of nth fibonacci: {}'.format(nthfibonacci(n)))
print('value of nth fibonacci: {}'.format(binetFibonacci(n)))
