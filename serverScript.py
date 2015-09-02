#! /usr/bin/python

# Echo server program
import socket
import RPi.GPIO as GPIO
import time
import SpeakerClass
import trafficLights

# set up the raspberry pi 2 board
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# pin assignment
greenLight = trafficLights.LED(16)
yellowLight = trafficLights.LED(20)
redLight = trafficLights.LED(21)
loudDoge = SpeakerClass.Speaker(18)


def startScript():
	greenLight.off()
	yellowLight.off()
	redLight.off()

	print("Running start up script...")
	redLight.on()
	loudDoge.playSound(392, .4)
	
	#time.sleep(0.3)
	redLight.off()
	yellowLight.on()
	loudDoge.playSound(587, .4)
	
	#time.sleep(0.3)
	yellowLight.off()
	greenLight.on()
	loudDoge.playSound(830, .4)
	
	#time.sleep(0.3)
	greenLight.off()
	yellowLight.on()
	loudDoge.playSound(587, .4)
	
	#time.sleep(0.3)
	yellowLight.off()
	redLight.on()
	loudDoge.playSound(392, .4)
	
	#time.sleep(0.3)
	redLight.off()
	
	time.sleep(0.5)
	greenLight.on()
	yellowLight.on()
	redLight.on()
	
	time.sleep(0.5)
	greenLight.off()
	yellowLight.off()
	redLight.off()
	
	time.sleep(0.5)
	greenLight.on()
	yellowLight.on()
	redLight.on()

	time.sleep(0.5)
	greenLight.off()
	yellowLight.off()
	redLight.off()
	print("Ready to doge some traffic light signals\n\n")
	for x in range (0,200,10):
		loudDoge.playSound(200+x, .05)




HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(3)

# start script
startScript()
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
			loudDoge.playSound(830, .3)
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
			loudDoge.playSound(587, .3)

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
			loudDoge.playSound(392, .3)

		elif data == "red_off":
			#finalMessage = "no {}".format(data)
			conn.sendall("Received: Turn Red Off")
			GPIO.output(redPin, GPIO.LOW)
			print ("Green: *\nYellow: *\nRed: 0\n")	

		#elif data == "close":
			#conn.sendall("Connection Closed")
			#conn.close()
			#break
	#conn.close()

except KeyboardInterrupt:
	GPIO.output(greenPin, GPIO.LOW)
	GPIO.output(yellowPin, GPIO.LOW)
	GPIO.output(redPin, GPIO.LOW)
	GPIO.cleanup()
	#conn.close()
	