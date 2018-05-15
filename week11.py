# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 10:30:43 2017

@author: Suharshith
"""

"""
LEc 12"""

num = 1
L = [5, 0, 2, 4, 6, 3, 1]
val = 0
for i in range(0, num):
    val = L[L[val]]

print(val)

def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

def search1(L, e):
    for i in L:
        if i == e:
            return True
        if i > e:
            return False  
    return False
"""same answer as search """

def search2(L, e):
    for i in L:
        if i == e:
            return True
        elif i > e:
            return False
    return False
"""same answer as search """


def search3(L, e):
    if L[0] == e:
        return True
    elif L[0] > e:
        return False
    else:
        return search3(L[1:], e)
    
""" search and search3 return the same answers provided L is non-empty and e is in L. correct  """

"""so correct function is """
#def search3(L, e):
#    # Test if the list is empty - if it is, e cannot be in it!
#    # Run this test first - so that we don't throw an error trying
#    #  to access L[0].
#    if L == []:
#        return False
#
#    if L[0] == e:
#        return True
#    elif L[0] > e:
#        return False
#    else:
#        return search3(L[1:], e)



def mySort(L):
    """ L, list with unique elements """
    clear = False
    while not clear:
        clear = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                clear = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
                
test = [1, 5, 3, 8, 4, 9, 6, 2]

 #mySort(test)
 
test = [1, 2, 3, 4, 5, 6, 8, 9]

def newSort(L):
    """ L, list with unique elements """
    for i in range(len(L) - 1):
        j=i+1
        while j < len(L):
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
            j += 1


