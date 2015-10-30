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
def buttonGreenOn(channel):
	shireTrafficLight.turnAllOff()
	shireTrafficLight.greenON()
	shireTrafficLight.printStatus()
def buttonYellowOn(channel):
	shireTrafficLight.turnAllOff()
	shireTrafficLight.yellowON()
	shireTrafficLight.printStatus()
def buttonRedOn(channel):
	shireTrafficLight.turnAllOff()
	shireTrafficLight.redON()
	shireTrafficLight.printStatus()
#def startupButton(channel):
#	shireTrafficLight.turnAllOff()
#	shireTrafficLight.startup(0)
#	shireTrafficLight.printStatus()


# pin assignment
phyGreenPin = 12
TCP_Green = 16
phyYellowPin = 23
TCP_Yellow = 20
phyRedPin = 24
TCP_Red = 21
speakerPin = 18
reset_startupScript = 26

#Instantiations and pin set up
shireTrafficLight = masterTrafficLight.trafficLight(TCP_Green,TCP_Yellow,TCP_Red,speakerPin)
GPIO.setup(phyGreenPin, GPIO.IN)
GPIO.setup(phyYellowPin, GPIO.IN)
GPIO.setup(phyRedPin, GPIO.IN)
#GPIO.setup(reset_startupScript, GPIO.IN)

# event handling
GPIO.add_event_detect(phyGreenPin, GPIO.FALLING, callback=buttonGreenOn, bouncetime = 500)
GPIO.add_event_detect(phyYellowPin, GPIO.FALLING, callback=buttonYellowOn, bouncetime = 500)
GPIO.add_event_detect(phyRedPin, GPIO.FALLING, callback=buttonRedOn, bouncetime = 500)
#GPIO.add_event_detect(reset_startupScript, GPIO.FALLING, callback=startupButton, bouncetime = 500)

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
		
		elif data == "random_set":
			conn.sendall("Received: Randomize")
			shireTrafficLight.randomize()
			#conn.sendall("Completed Randomize")
			shireTrafficLight.printStatus()

		#elif data == "close":
			#conn.sendall("Connection Closed")
			#conn.close()
			#break
	#conn.close()

except KeyboardInterrupt:
	shireTrafficLight.turnAllOff()
	GPIO.cleanup()
	print("Bye Bye!\n")
	exit()
	#conn.close()
	
