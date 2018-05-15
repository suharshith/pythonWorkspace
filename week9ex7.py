# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 17:15:44 2017

@author: Suharshith
"""

class A(object):
    def __init__(self):
        self.a = 1
    def x(self):
        print("A.x")
    def y(self):
        print("A.y")
    def z(self):
        print("A.z")

class B(A):
    def __init__(self):
        A.__init__(self)
        self.a = 2
        self.b = 3
    def y(self):
        print("B.y")
    def z(self):
        print("B.z")

class C(object):
    def __init__(self):
        self.a = 4
        self.c = 5
    def y(self):
        print("C.y")
    def z(self):
        print("C.z")

class D(C, B):
    def __init__(self):
        C.__init__(self)
        B.__init__(self)
        self.d = 6
    def z(self):
        print("D.z")
        


'''
In [164]: obj = D()

In [165]: print(obj.a)
2

In [166]: print(obj.b)
3

In [167]: print(obj.c)
5

In [168]: print(obj.d)
6

In [169]: obj.x()
A.x

In [170]: obj.y()
C.y

In [171]: obj.z()
D.z
'''