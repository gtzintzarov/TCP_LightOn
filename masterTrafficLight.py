#! /usr/bin/python

import RPi.GPIO as GPIO
import trafficLights
import SpeakerClass

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

	def startup(self):
		self.turnAllOff()

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
		self.turnAllOff(0)
		
		time.sleep(0.5)
		self.turnAllOn(0)

		time.sleep(0.5)
		self.turnAllOff(0)

		# startup tone
		print("Ready to doge some traffic light signals\n\n")
		for x in range (0,200,10):
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
		else
			self.greenON(0)
			self.yellowON(0)
			self.redON(0)

	def turnAllOff(self):
		self.greenOFF()
		self.yellowON()
		self.redOFF()

	def printStatus(self):
		print ("Green: {:#d}".format(self.greenStatus))
		print ("Yellow: {:#d}".format(self.yellowStatus))
		print ("Red: {:#d}\n".format(self.redStatus))