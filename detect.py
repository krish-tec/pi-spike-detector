
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(3, GPIO.OUT)         #LED output pin
j = 0
GPIO.output(3,0)
relayStatus = 0
while True:
       i=GPIO.input(13)
       if i==0:                 
             print j,": No Spike Detected",i, " relayStatus=",relayStatus
	     j+=1
	     if relayStatus != 0:
             	GPIO.output(3, 0)  #Turn OFF LED
             	print "OFF After ON"
		#time.sleep(0.1)
		relayStatus = 0
	     time.sleep(0.1)
       elif i==1:
	     print j,": Spike detected",i
	     j+=1
	     if relayStatus != 1:
             	GPIO.output(3, 1)  #Turn ON LED
	     	print "Relay ON"
             	time.sleep(5)
		relayStatus = 1
