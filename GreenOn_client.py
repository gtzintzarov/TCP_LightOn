#! /usr/bin/python

# Echo client program
import socket

HOST = '98.252.248.93'    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall("green_on")
data = s.recv(1024)
s.close()
print repr(data)