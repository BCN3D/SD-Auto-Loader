# -*- encoding: utf-8 -*-
#SD Auto Loader - Enric Gómez Pitarch & Marc Cobler
#BCN3D Technologies - Fundacio CIM

#This Program lets you to copy the files you want to multiple SD Cards
#It has 4 rocker switches to select the folders and documents to upload and
#a load button to start the sequence. First it checks if there is internet 
#to pull updates from Github.

import RPi.GPIO as GPIO
import time
import os
import sys
import socket

BCN3DSigmaPath = "/home/pi/BCN3DSigma"
BCN3DPlusPath = "/home/pi/BCN3DPlus"
repoPath = "/home/pi/sd-auto-loader"	

def haveInternet():
	REMOTE_SERVER = "www.google.com"
	try:
		host = socket.gethostbyname(REMOTE_SERVER)
		s = socket.create_connection((host, 443))
		return True
	except:
		pass
	return False 
	
def syncGithub():
	#Update the Repo
	if haveInternet():
		print "Internet is ON!"
		try:
			print "Getting updates from Github"
			os.chdir(repoPath)
			currentDirectory = os.getcwd()
			print "The current directory is: %s" % currentDirectory
			os.system("git pull origin master")
		except:
			print "Something went wrong, check your internet connection"
			pass
	else:
		print "No internet, no github sync" 
		
def manageInputs():
	print "Setting the switches to inputs"
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	#Set pull-ups to pins
	GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	#Read inputs just one time 
	input_state_5 = GPIO.input(5)
	input_state_26 = GPIO.input(26)
	input_state_19 = GPIO.input(19)
	input_state_13 = GPIO.input(13)
	input_state_6 = GPIO.input(6) 
	
def startUpLEDS():
	#Just a sequence of LEDs to know that the system is running the program
	print "Lightning some LEDs..."
	for x in range(0,4):
		#GPIO.setmode(GPIO.BCM)
		print "."
		GPIO.setup(21, GPIO.OUT)
		GPIO.output(21, GPIO.HIGH) #Status 1 
		GPIO.setup(20, GPIO.OUT)
		GPIO.output(20, GPIO.HIGH) #Status 2
		GPIO.setup(16, GPIO.OUT)		
		GPIO.output(16, GPIO.HIGH) #Status 3        
		GPIO.setup(12, GPIO.OUT)
		GPIO.output(12, GPIO.HIGH) #Status 4      
		GPIO.setup(7, GPIO.OUT)
		GPIO.output(7, GPIO.HIGH) #Status 5        
		GPIO.setup(8, GPIO.OUT)	
		GPIO.output(8, GPIO.HIGH) #Status 6        
		GPIO.setup(25, GPIO.OUT)
		GPIO.output(25, GPIO.HIGH) #Status 7       
		GPIO.setup(24, GPIO.OUT)
		GPIO.output(24, GPIO.HIGH) #Status 8        
		GPIO.setup(23, GPIO.OUT)
		GPIO.output(23, GPIO.HIGH) #Status 9 
		time.sleep(0.5)
		GPIO.output(21, GPIO.LOW)
		GPIO.output(20, GPIO.LOW)
		GPIO.output(16, GPIO.LOW)
		GPIO.output(12, GPIO.LOW)
		GPIO.output(7, GPIO.LOW)
		GPIO.output(8, GPIO.LOW)
		GPIO.output(25, GPIO.LOW)
		GPIO.output(24, GPIO.LOW)
		GPIO.output(23, GPIO.LOW) 
		
def loadBCN3DSigmaSD():
	time.sleep(15)
	os.system("./sd1FAT32") 
	GPIO.setup(21, GPIO.OUT)
	GPIO.output(21, GPIO.HIGH) #Status 1
	os.system("./sd2FAT32") 
	GPIO.setup(20, GPIO.OUT) 
	GPIO.output(20, GPIO.HIGH) #Status 2
	os.system("./sd3FAT32") 
	GPIO.setup(16, GPIO.OUT)
	GPIO.output(16, GPIO.HIGH) #Status 3
	os.system("./sd4FAT32") 
	GPIO.setup(12, GPIO.OUT)
	GPIO.output(12, GPIO.HIGH) #Status 4
	os.system("./sd5FAT32") 
	GPIO.setup(7, GPIO.OUT)
	GPIO.output(7, GPIO.HIGH) #Status 5
	os.system("./sd6FAT32") 
	GPIO.setup(8, GPIO.OUT)
	GPIO.output(8, GPIO.HIGH) #Status 6
	os.system("./sd7FAT32") 
	GPIO.setup(25, GPIO.OUT)
	GPIO.output(25, GPIO.HIGH) #Status 7
	os.system("./sd8FAT32") 
	GPIO.setup(24, GPIO.OUT)
	GPIO.output(24, GPIO.HIGH) #Status 8
	os.system("./sd9FAT32")
	GPIO.setup(23, GPIO.OUT)
	GPIO.output(23, GPIO.HIGH) #Status 9 
	time.sleep(2) #Sleep for 2 seconds
	GPIO.output(21, GPIO.LOW)
	GPIO.output(20, GPIO.LOW)
	GPIO.output(16, GPIO.LOW)
	GPIO.output(12, GPIO.LOW)
	GPIO.output(7, GPIO.LOW)
	GPIO.output(8, GPIO.LOW)
	GPIO.output(25, GPIO.LOW)	
	GPIO.output(24, GPIO.LOW)
	GPIO.output(23, GPIO.LOW)

def loadBCN3DSigmaScreenSD():
	time.sleep(15)
	os.system("./sd1FAT16")
	GPIO.setup(21, GPIO.OUT)
	GPIO.output(21, GPIO.HIGH) #Status 1
	os.system("./sd2FAT16")
	GPIO.setup(20, GPIO.OUT)
	GPIO.output(20, GPIO.HIGH) #Status 2
	os.system("./sd3FAT16")
	GPIO.setup(16, GPIO.OUT)
	GPIO.output(16, GPIO.HIGH) #Status 3
	os.system("./sd4FAT16")
	GPIO.setup(12, GPIO.OUT)
	GPIO.output(12, GPIO.HIGH) #Status 4
	os.system("./sd5FAT16")
	GPIO.setup(7, GPIO.OUT)
	GPIO.output(7, GPIO.HIGH) #Status 5
	os.system("./sd6FAT16")
	GPIO.setup(8, GPIO.OUT)
	GPIO.output(8, GPIO.HIGH) #Status 6
	os.system("./sd7FAT16")
	GPIO.setup(25, GPIO.OUT)
	GPIO.output(25, GPIO.HIGH) #Status 7
	os.system("./sd8FAT16")
	GPIO.setup(24, GPIO.OUT)
	GPIO.output(24, GPIO.HIGH) #Status 8
	os.system("./sd9FAT16")
	GPIO.setup(23, GPIO.OUT)
	GPIO.output(23, GPIO.HIGH) #Status 9
	time.sleep(2) #Sleep for 2 seconds
	GPIO.output(21, GPIO.LOW)
	GPIO.output(20, GPIO.LOW)
	GPIO.output(16, GPIO.LOW)
	GPIO.output(12, GPIO.LOW)
	GPIO.output(7, GPIO.LOW)
	GPIO.output(8, GPIO.LOW)
	GPIO.output(25, GPIO.LOW)
	GPIO.output(24, GPIO.LOW)
	GPIO.output(23, GPIO.LOW)


def loadBCN3DPlusSD():
	time.sleep(15)
	os.system("./sd1Plus") 
	GPIO.setup(21, GPIO.OUT)
	GPIO.output(21, GPIO.HIGH) #Status 1
	os.system("./sd2Plus")
	GPIO.setup(20, GPIO.OUT)
	GPIO.output(20, GPIO.HIGH) #Status 2
	os.system("./sd3Plus")
	GPIO.setup(16, GPIO.OUT)
	GPIO.output(16, GPIO.HIGH) #Status 3
	os.system("./sd4Plus")
	GPIO.setup(12, GPIO.OUT)
	GPIO.output(12, GPIO.HIGH) #Status 4
	os.system("./sd5Plus")
	GPIO.setup(7, GPIO.OUT)
	GPIO.output(7, GPIO.HIGH) #Status 5
	os.system("./sd6Plus")
	GPIO.setup(8, GPIO.OUT)
	GPIO.output(8, GPIO.HIGH) #Status 6
	os.system("./sd7Plus")
	GPIO.setup(25, GPIO.OUT)
	GPIO.output(25, GPIO.HIGH) #Status 7
	os.system("./sd8Plus")
	GPIO.setup(24, GPIO.OUT)
	GPIO.output(24, GPIO.HIGH) #Status 8
	os.system("./sd9Plus")
	GPIO.setup(23, GPIO.OUT)
	GPIO.output(23, GPIO.HIGH) #Status 9
	time.sleep(2) #Sleep for 2 seconds
	GPIO.output(21, GPIO.LOW)
	GPIO.output(20, GPIO.LOW)
	GPIO.output(16, GPIO.LOW)
	GPIO.output(12, GPIO.LOW) 
	GPIO.output(7, GPIO.LOW)
	GPIO.output(8, GPIO.LOW)
	GPIO.output(25, GPIO.LOW)
	GPIO.output(24, GPIO.LOW)
	GPIO.output(23, GPIO.LOW) 
	
def printButtonStatus():
	print "Switch 1 is set to: %d" % GPIO.input(6)
	print "Switch 2 is set to: %d" % GPIO.input(13)
	print "Switch 3 is set to: %d" % GPIO.input(19)
	print "Switch 4 is set to: %d" % GPIO.input(26)

def checkButtons(channel):
	#Read the status of the switches and buttons
	try:
		print "Reading the switch buttons..."
		input_state_26 = GPIO.input(26)
		input_state_19 = GPIO.input(19)
		input_state_13 = GPIO.input(13)
		input_state_6 = GPIO.input(6)
		printButtonStatus()
		
		if input_state_26 == False and input_state_19 == True and input_state_13 == True and input_state_6 == True:
			print 'Loading BCN3D Sigma SD'
			loadBCN3DSigmaSD()				 
			time.sleep(2)
		if input_state_26 == True and input_state_19 == False and input_state_13 == True and input_state_6 == True:
			print 'Loading BCN3D Sigma Display uSD' 
			loadBCN3DSigmaScreenSD()     
			time.sleep(2)
		if input_state_26 == True and input_state_19 == True and input_state_13 == False and input_state_6 == True:
			print 'Loading BCN3D+ SD' 
			loadBCN3DSigmaSD()
			time.sleep(2)
		#if input_state_26 == True and input_state_19 == True and input_state_13 == True and input_state_6 == False:
			
		
	except KeyboardInterrupt:
		#If we press ctrl + c
		print "Program closed by user"
		GPIO.cleanup()
		sys.exit()
	except:
		print "Other error or exception ocurred!"
		GPIO.cleanup()
		sys.exit() 
		
		
#Main program
def main():
	syncGithub()
	manageInputs()
	startUpLEDS()
	#Callback function in PIN 5. Whenever a Falling Edge is detected, run checkButtons function
	GPIO.add_event_detect(5, GPIO.FALLING, callback=checkButtons, bouncetime=300)

	while True:
		time.sleep(5)
		print "waiting for the load button..."		

#Just the regular boilerplate to start the program
if __name__ == '__main__':
	main()
