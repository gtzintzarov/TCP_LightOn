#! /usr/bin/python

# Echo client program
import socket

HOST = '10.0.1.17'    # The remote host
PORT = 50007              # The same port as used by the server
while 1:
    turnOn_Off = input("\nEnter (0/1) for on or off: ")
    if turnOn_Off == 1:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        s.sendall('1')
        data = s.recv(1024)
        s.close()
        print repr(data)
    elif turnOn_Off == 0:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        s.sendall('0')
        data = s.recv(1024)
        s.close()
        print repr(data)
