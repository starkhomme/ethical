#!/bin/python3

import socket

HOST=input('enter host name \n')
PORT=int(input('enter port \n'))

s=socket.socket()
try:
    s.connect((HOST,PORT))
    print('connected '+HOST)

except:
    print('could not make connection')
