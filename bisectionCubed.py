# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 17:52:35 2017

@author: Suharshith
"""

cube = 54
epsilon = 0.01
num_guesses = 0
low = 0
high = cube
guess = (high + low)/2.0
while abs(guess**3 - cube) >= epsilon:
    print('low= '+ str(low) + ' high = '+ str(high) + ' ans= ' + str(ans))
    if guess**3 < cube :
        low = guess
    else:
        high = guess
    guess = (high + low)/2.0
    num_guesses += 1
print('num_guesses =', num_guesses)
print(guess, 'is close to the cube root of', cube)

