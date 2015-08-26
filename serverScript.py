#! /usr/bin/python

# Echo server program
import socket
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.OUT)



HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
while 1:
	conn, addr = s.accept()
	#print 'Connected by', addr
	#while 1:
    	data = conn.recv(1024)
	print data
	if data == "1":
		#print repr(data)
    		if not data: break
		#finalMessage = "{}".format(data)
   		conn.sendall("Received: Turn on bulb")
		GPIO.output(19, GPIO.HIGH)
	elif data == "0":
		#finalMessage = "no {}".format(data)
		conn.sendall("Received: Turn off bulb")
		GPIO.output(19, GPIO.LOW)	
conn.close()
