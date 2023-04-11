import RPi.GPIO as gp
import time
import sys

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

gp.setmode(gp.BCM)

gp.setup(dac, gp.OUT)
gp.setup(troyka, gp.OUT, initial=gp.HIGH)
gp.setup(comp, gp.IN)

def dec2bin(val):
    return [int(i) for i in bin(val)[2:].zfill(8)]

def abc():
    for i in range(256):
        gp.output(dac, dec2bin(i))
        time.sleep(0.05)
        if not gp.input(comp):
            return i
    return 0
    
try:
    while True:
        a = abc()
        print(3.3 * a / 255)

finally:
    gp.output(dac, 0)
    gp.cleanup()