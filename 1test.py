import RPi.GPIO as GPIO
import time
import serial
import os
# Enable Serial Communication
port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def blink():
    a = GPIO.input(5)
    if a == False:
        return 0.1
    else:
        return 1


# Transmitting AT Commands to the Modem
# '\r\n' indicates the Enter key

port.write('AT' + '\r\n')
rcv = port.read(10)
print rcv

e = 0
while True:
        GPIO.output(7, 0)
        time.sleep(blink())
        GPIO.output(7, 1)
        time.sleep(blink())


GPIO.cleanup()
#GPIO.cleanup()

#GPIO.output(7,0)
#GPIO.cleanup() 
