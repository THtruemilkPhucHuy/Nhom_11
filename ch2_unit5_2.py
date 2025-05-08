from gpiozero import LED
from gpiozero import DistanceSensor
import time

sensor = DistanceSensor(echo = 23, trigger = 24)
red = LED(14)
amber = LED(15)
green = LED(18)
while True:
    # distance in decimeters
    distance = sensor.distance * 100
    print("distance : ", distance)
    if distance < 20:
        red.on()
        amber.off()
        green.off()
    elif distance > 80:
        red.off()
        amber.off()
        green.on()
    else:
        red.off()
        amber.on()
        green.off()
    time.sleep(0.2)

