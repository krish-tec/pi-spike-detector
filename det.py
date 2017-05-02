
#!/usr/bin/env python2.7

# file: wait_for_edge-both-fix.py
#
# wait_for_edge solution for falling & rising edges (both)
# a falling edge is detected at approx. 1.16V, a rising edge at approx. 1.25V
#
# caveat:
# if you use the timeout parameter, the active edge will be shown after the timeout
# you cannot use GPIO.remove_event_detect(Input_Sig)
#
__author__ = 'paulv'

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

Input_Sig = 23 # any plain GPIO pin
GPIO.setup(Input_Sig, GPIO.IN)


def main():

    try:
        while True:
            pass # your code

            #  setup the edge detection
            GPIO.wait_for_edge(Input_Sig, GPIO.RISING)

            # if we're here, an edge was recognized
            sleep(0.005) # debounce for 5mSec
            # only show valid edges
            if GPIO.input(Input_Sig) == 1:
                print "RISING"
            else:
                print "FALLING"


    except KeyboardInterrupt:
        pass
    finally:
        print "\nRelease the used pin(s)"
        GPIO.cleanup([Input_Sig])


if __name__ == '__main__':
    main()
