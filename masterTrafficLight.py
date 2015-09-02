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

	def startup():
		self.turnAllOff()

		print("Running start up script...")
		self.redLight.on()
		self.loudDoge.playSound(392, .4)
		
		#time.sleep(0.3)
		self.redLight.off()
		self.yellowLight.on()
		self.loudDoge.playSound(587, .4)
		
		#time.sleep(0.3)
		self.yellowLight.off()
		self.greenLight.on()
		self.loudDoge.playSound(830, .4)
		
		#time.sleep(0.3)
		self.greenLight.off()
		self.yellowLight.on()
		self.loudDoge.playSound(587, .4)
		
		#time.sleep(0.3)
		self.yellowLight.off()
		self.redLight.on()
		self.loudDoge.playSound(392, .4)
		
		#time.sleep(0.3)
		self.redLight.off()
		
		time.sleep(0.5)
		self.turnAllOn()
		
		time.sleep(0.5)
		self.turnAllOff()
		
		time.sleep(0.5)
		self.turnAllOn()

		time.sleep(0.5)
		self.turnAllOff()

		# startup tone
		print("Ready to doge some traffic light signals\n\n")
		for x in range (0,200,10):
			self.loudDoge.playSound(200+x, .05)

	def greenON():
		self.greenLight.on()
		self.loudDoge.playSound(830, .3)
		self.greenStatus = True

	def greenOFF():
		self.greenLight.off()
		self.greenStatus = False

	def yellowON():
		self.yellowLight.on()
		self.loudDoge.playSound(587, .3)
		self.yellowStatus = True

	def yellowOFF():
		self.yellowLight.off()
		self.yellowStatus = False

	def redON():
		self.redLight.on()
		self.loudDoge.playSound(392, .3)
		self.redStatus = True

	def redOFF():
		self.redLight.off()
		self.redStatus = False

	def turnAllOn():
		self.greenON()
		self.yellowON()
		self.redON()

	def turnAllOff():
		self.greenOFF()
		self.yellowON()
		self.redOFF()

	def printStatus():
		print ("Green: {:#d}".format(self.greenStatus))
		print ("Yellow: {:#d}".format(self.yellowStatus))
		print ("Red: {:#d}\n".format(self.redStatus))