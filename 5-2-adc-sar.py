import RPi.GPIO as gp
import time

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
def adc():
    k = 0
    for i in range(7, -1, -1):
        k+= 2**i
        gp.output(dac, dec2bin(k))
        time.sleep(0.01)
        if not gp.input(comp):
            k -= 2**i
    return k
    
try:
    while True:
        a = adc()
        print(3.3 * a / 255)

finally:
    gp.output(dac, 0)
    gp.cleanup()