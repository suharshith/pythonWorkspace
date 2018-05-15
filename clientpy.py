# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 17:30:47 2018

@author: Suharshith
"""

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

s.connect(host, port)
print s.recv(1024)
s.close                     # Close the socket when done