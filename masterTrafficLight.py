#! /usr/bin/python

import RPi.GPIO as GPIO
import trafficLights
import SpeakerClass
import time
import random

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)




# This creates the trafficlight class
class trafficLight:
	def __init__(self, _greenPin, _yellowPin, _redPin, _speakerPin):
		self.greenLight = trafficLights.light(_greenPin)
		self.yellowLight = trafficLights.light(_yellowPin)
		self.redLight = trafficLights.light(_redPin)
		self.loudDoge = SpeakerClass.Speaker(_speakerPin)

		self.greenStatus = False
		self.yellowStatus = False
		self.redStatus = False

		self.startup()

	def startup(self, starting=1):
		self.turnAllOff()

		if starting == 1:
			print("Running start up script...")
		self.redON()
		
		#time.sleep(0.3)
		self.redOFF()
		self.yellowON()
		
		#time.sleep(0.3)
		self.yellowOFF()
		self.greenON()
		
		#time.sleep(0.3)
		self.greenOFF()
		self.yellowON()
		
		#time.sleep(0.3)
		self.yellowOFF()
		self.redON()
		
		#time.sleep(0.3)
		self.redOFF()
		
		time.sleep(0.5)
		self.turnAllOn(0)
		
		time.sleep(0.5)
		self.turnAllOff()
		
		time.sleep(0.5)
		self.turnAllOn(0)

		time.sleep(0.5)
		self.turnAllOff()

		# startup tone
		if starting == 1:
			print("Ready to doge some traffic light signals\n\n")
		for x in range (0,200,6):
			self.loudDoge.playSound(200+x, .05)
		

	def greenON(self, sound = 1):
		self.greenLight.on()
		self.greenStatus = True
		if sound == 1:
			self.loudDoge.playSound(830, .3)

	def greenOFF(self):
		self.greenLight.off()
		self.greenStatus = False

	def yellowON(self , sound = 1):
		self.yellowLight.on()
		self.yellowStatus = True
		if sound == 1:
			self.loudDoge.playSound(587, .3)

	def yellowOFF(self):
		self.yellowLight.off()
		self.yellowStatus = False

	def redON(self, sound = 1):
		self.redLight.on()
		self.redStatus = True
		if sound == 1:
			self.loudDoge.playSound(392, .3)

	def redOFF(self):
		self.redLight.off()
		self.redStatus = False

	def turnAllOn(self, sound = 1):
		if sound == 1:
			self.greenON(1)
			self.yellowON(1)
			self.redON(1)
		else:
			self.greenON(0)
			self.yellowON(0)
			self.redON(0)

	def turnAllOff(self):
		self.greenOFF()
		self.yellowOFF()
		self.redOFF()

	def nextLight(self):
		if self.redStatus:
			self.redOFF()
			self.yellowON(0)
		elif self.yellowStatus:
			self.yellowOFF()
			self.greenON(0)
		elif self.greenStatus:
			self.greenOFF()
			self.redON(0)
		else:
			self.greenON(0)

	def randomize(self):
		#self.nextLight()
		self.seed = int((random.random())*20 + 10)
		self.counter=0
		#print("{}".format(self.seed))
		while self.counter < self.seed:
			#print("{}".format(self.counter))
			self.nextLight()
			time.sleep(.05)
			self.counter = self.counter + 1


	def printStatus(self):
		print ("Red: {:#d}".format(self.redStatus))
		print ("Yellow: {:#d}".format(self.yellowStatus))
		print ("Green: {:#d}\n".format(self.greenStatus))
		return ("{:#d} {:#d} {:#d}".format(self.greenStatus,self.yellowStatus, self.redStatus))