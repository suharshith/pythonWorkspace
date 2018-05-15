# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 17:26:18 2018

@author: Suharshith
"""
import socket

s = socket.socket()
host = socket.gethostname()
port = 12345

s.bind((host, port))


s.listen()
while True:
   c, addr = s.accept()     # Establish connection with client.
   print 'Got connection from', addr
   c.send('Thank you for connecting')
   c.close()               