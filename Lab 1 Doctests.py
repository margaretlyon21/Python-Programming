#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Four Required questions for Lab 1."""

_author_ = "Maggie Lyon"
_credits_ = ["None"]
_email_ = "lyonme@mail.uc.edu" 

# RQ1
def mult_inverse(x, y):
    """Returns True if the product of x and y is one.

    >>> mult_inverse(-1, 1)
    False
    >>> mult_inverse(1, 2)
    False
    >>> mult_inverse(-2, -1/2)
    True
    """
    if (x*y == 1):
        return True
    else:
        return False

 
## while Loops ##
# RQ2
def not_factor (n):
    """Prints out all of the numbers that do not divide `n` evenly.
 
    >>> not_factor(10)
    9
    8
    7
    6
    4
    3
    """
    x = n
    while x > 0:
        if (n % x == 0):
            x -= 1
        else:
            print(x)
            x -=1
    
# RQ3
def lucas(n):
    """Returns the nth Lucas number.
      Lucas numbers form a series similar to Fibonacci series, 
      where each number is the sum of the previous two numbers:
      2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199, 322, 521, 843,...
 
    >>> lucas(0)
    2
    >>> lucas(1)
    1
    >>> lucas(2)
    3
    >>> lucas(100)
    792070839848372253127
    """
    lucasseries = [2,1]
    i = 1
    while i < n:
        lucasseries.append(lucasseries[i]+lucasseries[i-1])
        i += 1
    print(lucasseries[n])

#RQ4
def gets_discount(p1, p2, p3):
    """ Returns True if p1 is an adult (age at least 18) and both of p2 and p3 are children (age 12 or below), 
    False otherwise. Do not use an if statement.
    >>> gets_discount(15, 12, 11)
    False
    >>> gets_discount(90, 11, 12)
    True
    """
    while (p1 >= 18 and p2 < 18 and p3 <18):
        return True
    while (p1 < 18 or p2 >= 18 or p3 >= 18):
        return False

    
import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)
