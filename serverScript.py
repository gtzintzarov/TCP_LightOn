#! /usr/bin/python

# Echo server program
import socket
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

greenPin = 36;
yellowPin = 38;
redPin = 40;

GPIO.setup(greenPin, GPIO.OUT) #Green
GPIO.setup(yellowPin, GPIO.OUT) #Yellow
GPIO.setup(redPin, GPIO.OUT) #Red


def startScript():
	print("Running start up script...")
	GPIO.output(redPin, GPIO.HIGH)
	time.sleep(0.3)
	GPIO.output(redPin, GPIO.LOW)
	GPIO.output(yellowPin, GPIO.HIGH)
	time.sleep(0.3)
	GPIO.output(yellowPin, GPIO.LOW)
	GPIO.output(greenPin, GPIO.HIGH)
	time.sleep(0.3)
	GPIO.output(greenPin, GPIO.LOW)
	GPIO.output(yellowPin, GPIO.HIGH)
	time.sleep(0.3)
	GPIO.output(yellowPin, GPIO.LOW)
	GPIO.output(redPin, GPIO.HIGH)
	time.sleep(0.3)
	GPIO.output(redPin, GPIO.LOW)
	time.sleep(0.5)
	GPIO.output(greenPin, GPIO.HIGH)
	GPIO.output(yellowPin, GPIO.HIGH)
	GPIO.output(redPin, GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(greenPin, GPIO.LOW)
	GPIO.output(yellowPin, GPIO.LOW)
	GPIO.output(redPin, GPIO.LOW)
	time.sleep(0.5)
	GPIO.output(greenPin, GPIO.HIGH)
	GPIO.output(yellowPin, GPIO.HIGH)
	GPIO.output(redPin, GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(greenPin, GPIO.LOW)
	GPIO.output(yellowPin, GPIO.LOW)
	GPIO.output(redPin, GPIO.LOW)
	print("Ready to doge some traffic light signals\n\n")



HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

# start script
startScript()

while 1:
	conn, addr = s.accept()
	#print 'Connected by', addr
	#while 1:
	data = conn.recv(1024)

    #Turn ALL off
	if data == "all_off":
		#print repr(data)
   		#	if not data: break
		#finalMessage = "{}".format(data)
		conn.sendall("Received: Turn ALL OFF")
		GPIO.output(greenPin, GPIO.LOW)
		GPIO.output(yellowPin, GPIO.LOW)
		GPIO.output(redPin, GPIO.LOW)
		print ("Green: 0\nYellow: 0\nRed: 0\n")

	elif data == "all_on":
		#print repr(data)
   		#	if not data: break
		#finalMessage = "{}".format(data)
		conn.sendall("Received: Turn ALL ON")
		GPIO.output(greenPin, GPIO.HIGH)
		GPIO.output(yellowPin, GPIO.HIGH)
		GPIO.output(redPin, GPIO.HIGH)
		print ("Green: 1\nYellow: 1\nRed: 1\n")

    #Turn on/off green light
	elif data == "green_on":
		#print repr(data)
    	#	if not data: break
		#finalMessage = "{}".format(data)
		conn.sendall("Received: Turn Green On")
		GPIO.output(greenPin, GPIO.HIGH)
		print ("Green: 1\nYellow: *\nRed: *\n")
	elif data == "green_off":
		#finalMessage = "no {}".format(data)
		conn.sendall("Received: Turn Green Off")
		GPIO.output(greenPin, GPIO.LOW)
		print ("Green: 0\nYellow: *\nRed: *\n")

	#Turn on/off yellow light
	elif data == "yellow_on":
		#print repr(data)
    	#	if not data: break
		#finalMessage = "{}".format(data)
		conn.sendall("Received: Turn Yellow On")
		GPIO.output(yellowPin, GPIO.HIGH)
		print ("Green: *\nYellow: 1\nRed: *\n")
	elif data == "yellow_off":
		#finalMessage = "no {}".format(data)
		conn.sendall("Received: Turn Yellow Off")
		GPIO.output(yellowPin, GPIO.LOW)
		print ("Green: *\nYellow: 0\nRed: *\n")

	#Turn on/off red light
	elif data == "red_on":
		#print repr(data)
    	#	if not data: break
		#finalMessage = "{}".format(data)
		conn.sendall("Received: Turn Red On")
		GPIO.output(redPin, GPIO.HIGH)
		print ("Green: *\nYellow: *\nRed: 1\n")
	elif data == "red_off":
		#finalMessage = "no {}".format(data)
		conn.sendall("Received: Turn Red Off")
		GPIO.output(redPin, GPIO.LOW)
		print ("Green: *\nYellow: *\nRed: 0\n")	

	elif data == "close":
		conn.sendall("Connection Closed")
		conn.close()
		break
conn.close()