
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(3, GPIO.OUT)         #LED output pin
while True:
       i=GPIO.input(13)
       flag = 0
       if i==0:                 #When output from motion sensor is LOW
            # print "No intruders",i
             GPIO.output(3, 1)  #Turn OFF LED
             time.sleep(0.1)
       elif i==1:
	     if flag == 0:               #When output from motion sensor is HIGH
             	print "Spike detected",i
             	GPIO.output(3, 0)  #Turn ON LED
             	time.sleep(0.1)
		flag +=1
