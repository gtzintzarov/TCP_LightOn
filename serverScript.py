#! /usr/bin/python

# Echo server program
import socket
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

greenPin = 16;
yellowPin = 20;
redPin = 21;

GPIO.setup(greenPin, GPIO.OUT) #Green
GPIO.setup(yellowPin, GPIO.OUT) #Yellow
GPIO.setup(redPin, GPIO.OUT) #Red

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
	if data == "1":
		#print repr(data)
    		if not data: break
		#finalMessage = "{}".format(data)
   		conn.sendall("Received: Turn on bulb")
		GPIO.output(greenPin, GPIO.HIGH)
		print ("Light is on\n")
	elif data == "0":
		#finalMessage = "no {}".format(data)
		conn.sendall("Received: Turn off bulb")
		GPIO.output(greenPin, GPIO.LOW)
		print ("Light is off\n")	
conn.close()
