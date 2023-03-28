import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]

gpio.setup(dac, gpio.OUT)

def dec2bin(val):
    return [int(i) for i in bin(val)[2:].zfill(8)]
try:
    while True:
        
        n = input("Введите число: ")
        if n == "q":
            break
        if n.isdecimal():
            pass
        else:
            try:
                a = float(n)
                if a<0:
                    print("NEGATIVE")
                    continue
                print("DECIMAL")
                continue
            except:
                print("NOT NUMBER")
                continue 
        n = int(n)
        if n < 0:
            print("NEGATIVE")
            continue
        if n > 255:
            print("TOO MUCH")
            continue

        gpio.output(dac, dec2bin(n))
        print(n/255*3.3)
finally:
    gpio.output(dac,0)
    gpio.cleanup()