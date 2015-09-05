#! /usr/bin/python

# Echo server program
import socket
import RPi.GPIO as GPIO
import time
import SpeakerClass
import trafficLights
import masterTrafficLight

# set up the raspberry pi 2 board
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# bound listening port
HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(3)


# setup interupts
def switchAllOn(channel):
	print "Hi"
	#masterTrafficLight.turnAllOn()


# pin assignment
shireTrafficLight = masterTrafficLight.trafficLight(16,20,21,18)
GPIO.setup(12, GPIO.IN)

GPIO.add_event_detect(12, GPIO.FALLING, callback=switchAllOn)

# start main script
try:
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
			shireTrafficLight.turnAllOff()
			shireTrafficLight.printStatus()

		#Turn ALL on
		elif data == "all_on":
			#print repr(data)
	   		#	if not data: break
			#finalMessage = "{}".format(data)
			conn.sendall("Received: Turn ALL ON")
			shireTrafficLight.turnAllOn()
			shireTrafficLight.printStatus()

	    #Turn on/off green light
		elif data == "green_on":
			#print repr(data)
	    	#	if not data: break
			#finalMessage = "{}".format(data)
			conn.sendall("Received: Turn Green On")
			shireTrafficLight.greenON()
			shireTrafficLight.printStatus()
			

		elif data == "green_off":
			#finalMessage = "no {}".format(data)
			conn.sendall("Received: Turn Green Off")
			shireTrafficLight.greenOFF()
			shireTrafficLight.printStatus()
			

		#Turn on/off yellow light
		elif data == "yellow_on":
			#print repr(data)
	    	#	if not data: break
			#finalMessage = "{}".format(data)
			conn.sendall("Received: Turn Yellow On")
			shireTrafficLight.yellowON()
			shireTrafficLight.printStatus()
			

		elif data == "yellow_off":
			#finalMessage = "no {}".format(data)
			conn.sendall("Received: Turn Yellow Off")
			shireTrafficLight.yellowOFF()
			shireTrafficLight.printStatus()

		#Turn on/off red light
		elif data == "red_on":
			#print repr(data)
	    	#	if not data: break
			#finalMessage = "{}".format(data)
			conn.sendall("Received: Turn Red On")
			shireTrafficLight.redON()
			shireTrafficLight.printStatus()
			

		elif data == "red_off":
			#finalMessage = "no {}".format(data)
			conn.sendall("Received: Turn Red Off")
			shireTrafficLight.redOFF()
			shireTrafficLight.printStatus()

		elif data == "get_status":
			conn.sendall(shireTrafficLight.printStatus())
			#shireTrafficLight.printStatus()

		#elif data == "close":
			#conn.sendall("Connection Closed")
			#conn.close()
			#break
	#conn.close()

except KeyboardInterrupt:
	shireTrafficLight.turnAllOff()
	GPIO.cleanup()
	#conn.close()
	