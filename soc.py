#!/bin/python3

import socket

HOST='localhost'
PORT=7776

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))


