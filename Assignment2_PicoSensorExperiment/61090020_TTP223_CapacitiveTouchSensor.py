# Assignment 2.2: TTP223 Capacitive Touch Sensor for Pi Pico
# Docu: https://components101.com/ics/ttp223-single-channel-touch-detector-ic

# From Left->Right
# Yellow Cable: Sensor Signal Output - to PIN1
# Brown  Cable: 3.3 V VCC
# Blue   Cable: GND

import machine, utime

LedOnboard = machine.Pin(25,machine.Pin.OUT) # Board's LED
ON = 1
OFF = 0

CapacitiveTouchSensor = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_DOWN)
Buzzer = machine.Pin(1, machine.Pin.OUT)

def CapacitiveTouchHandler(pin):
    print("ALERT: Touched at" + str(utime.localtime()))
    Buzzer.value(ON)

CapacitiveTouchSensor.irq(trigger=machine.Pin.IRQ_RISING, handler=CapacitiveTouchHandler)

while True:
    LedOnboard.value(ON)
    utime.sleep(1) # delay 1 sec
    LedOnboard.value(OFF)
    utime.sleep(1) # delay 1 sec
    Buzzer.value(OFF)
