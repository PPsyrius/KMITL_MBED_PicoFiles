# Assignment 2.1: XKC-Y25-V Liquid Level (No-Contact) Sensor for Pi Pico
# Docu: https://www.robo-tank.ca/Non-Contact-Liquid-Level-Water-Sensor-KXC-Y25-V-Arduino

# From Left->Right
# Brown  Cable: 5V VCC
# Yellow Cable: Sensor Signal Output - to PIN1
# Blue   Cable: GND
# Black  Cable: Mode Selection (Unimplemented)

# Buzzer is connected to PIN2

import machine, utime

LedOnboard = machine.Pin(25,machine.Pin.OUT) # Board's LED
ON = 1
OFF = 0

WaterLevelSensor = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)
Buzzer = machine.Pin(1, machine.Pin.OUT)

def WaterLevelHandler(pin):
    print("ALERT: Water Reaches Critical Level at" + str(utime.localtime()))
    Buzzer.value(ON)

WaterLevelSensor.irq(trigger=machine.Pin.IRQ_RISING, handler=WaterLevelHandler)

while True:
    LedOnboard.value(ON)
    utime.sleep(1) # delay 1 sec
    LedOnboard.value(OFF)
    utime.sleep(1) # delay 1 sec
    Buzzer.value(OFF)
