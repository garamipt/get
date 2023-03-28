import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]

gpio.setup(dac + [2, 21, 20], gpio.OUT)
def dec2bin(val):
    return [int(i) for i in bin(val)[2:].zfill(8)]
p = gpio.PWM(2, 10000)
p.start(0)
gpio.output(20, 1)
try:
    while True:

        i = float(input("Введите заполнение"))
        p.ChangeDutyCycle(i)
finally:
    
    p.stop()
    gpio.output(dac,0)
    gpio.cleanup()