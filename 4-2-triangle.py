import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]

gpio.setup(dac, gpio.OUT)
sec = 10 / 512
def dec2bin(val):
    return [int(i) for i in bin(val)[2:].zfill(8)]

try:
    while True:
        for i in range(0, 256):
            gpio.output(dac, dec2bin(i))
            time.sleep(sec)
        for i in range(254, 0 ,-1):
            gpio.output(dac, dec2bin(i))
            time.sleep(sec)
finally:
    gpio.output(dac,0)
    gpio.cleanup()
