# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 20:34:31 2017

@author: Suharshith
"""


def square1(x):
    '''
    x: int or float.
    '''
    # Your code here
    return x**2
    


def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    # Your code here
    return((a*x**2 )+(b*x)+c)
    
    
    
def f( x ):
    x = x + 1
    print('in f(x): x =', x)
    return x
x = 30
z = f( x )



def func_a():
    print('inside func_a')
def func_b(y):
    print('inside func_b')
    return y
def func_c(z):
    print('inside func_c')
    return z()
print(func_a())
print(5 + func_b(2))
print(func_c(func_a))


def f(y):
    x = 1
    x += 1
    print(x)
x = 5
f(x)
print(x)



def g(y):
    print(x)
    print(x + 1)
x = 5
g(x)
print(x)


def h(y):
    x = x + 1
    x = 5
h(x)
print(x)




def a(x):
   '''
   x: int or float.
   '''
   return x + 1

def b(x):
   '''
   x: int or float.
   '''
   return x + 1.0
  
def c(x, y):
   '''
   x: int or float. 
   y: int or float.
   '''
   return x + y

def d(x, y):
   '''
   x: Can be of any type.
   y: Can be of any type.
   '''
   return x > y

def e(x, y, z):
   '''
   x: Can be of any type.
   y: Can be of any type.
   z: Can be of any type.
   '''
   return x >= y and x <= z

def f(x, y):
   '''
   x: int or float.
   y: int or float
   '''
   x + y - 2  
    
   
   
def a(x, y, z):
     if x:
         return y
     else:
         return z

def b(q, r):
    return a(q>r, q, r)


a = 10
def f(x):
   return x + a
a = 3
f(1)


x = 12
def g(x):
    x = x + 1
    def h(y):
        return x + y
    return h(6)
g(x)
 

def foo(x, y = 5):
   def bar(x):
      return x + 1
   return bar(y * 2)
          
foo(3)
 

def foo(x, y = 5):
   def bar(x):
      return x + 1
   return bar(y * 2)
          
foo(3, 0)


def foo (x):
   def bar (z, x = 0):
      return z + x
   return bar(3, x)

foo(2)


def foo (x):
   def bar (z, x = 0):
      return z + x
   return bar(3)

foo(5)


def fourthPower(x):
    return square1(square1(x))
     
def odd(x):
    '''
    x: int

    returns: True if x is odd, False otherwise
    '''
    # Your code here
    return x%2 != 0

"""
Keyword Arguments

"""


def printName(firstName, lastName, reverse):
    if reverse:
        print(lastName + ',' + firstName)
    else:
        print(firstName, lastName)
        
printName('Eric' , 'Grimson', False)

"""
Iterative mult

"""
def mult_iter(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result

mult_iter(10,5)

"""
Recursive mult
"""

def mult(a, b):
    if b == 1:
        return a
    else:
        return a + mult(a,b-1)
  
"""
  Factorial
  
"""  
def fact(n):
    if n ==1:
        return 1
    else:
        return n*fact(n-1)
    
print(fact(4))

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    result = base
    if exp == 0:
        return 1
    else:
        for i in range(1,exp):
            result *= base
    return result


def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp ==0:
        return 1
    else:
        return base * recurPower(base, exp-1)
    

def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)

print(Towers(4, 'P1', 'P2', 'P3'))




def gcdIter(a, b):
    '''
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    gcd = 1
    c = min(a, b)
    for i in range(c, 1, -1):
        if (a % i == 0) and (b % i == 0):
            gcd = i
            break
        else:
            gcd = 1
    return gcd

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcdRecur(b, a % b)
    
    
    """
    Fibonacci Series
    
    """
def fib(x):
    if x == 0 or x==1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

"""
Palindrome

"""
def isPalindrome(s):

    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChars(s))

print("")
print('Is eve a palindrome?')
print(isPalindrome('eve'))

print('')
print('Is able was I ere I saw Elba a palindrome?')
print(isPalindrome('Able was I, ere I saw Elba'))
    

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    
    if aStr == "":
        return False
    elif len(aStr) == 1 and aStr == char:
        return True
    elif len(aStr) == 1 and aStr != char:
        return False
    elif aStr[len(aStr)//2] == char:
        return True
    else:
        if char < aStr[len(aStr)//2]:
            return isIn(char, aStr[:len(aStr)//2])
        else:
            return isIn(char, aStr[len(aStr)//2:])
        
        
def polysum(n,s):
        
    from math import tan, pi
    area = (0.25*n*s**2)/tan(pi/n)
    perimeter = n * s
    return round(area+perimeter**2,4)