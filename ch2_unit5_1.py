from gpiozero import LED
from gpiozero import Button

button = Button(23)
red = LED(14)
amber = LED(15)
green = LED(18)
leds = [green, amber, red]
idx = 0

for i in range(len(leds)):
    if i == idx:
        leds[idx].on()
    else:
        leds[idx].off()

while True:
    if button.when_pressed:
        idx = (idx + 1) % len(leds)
    for i in range(len(leds)):
        if i == idx:
            leds[idx].on()
        else:
            leds[idx].off()


