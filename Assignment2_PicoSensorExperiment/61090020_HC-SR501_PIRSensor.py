# Assignment 2.3: HC-SR501 PiezoElectric Sensor for Pi Pico
# Docu: https://components101.com/hc-sr501-pir-sensor

# Blue   Cable: GND
# Yellow Cable: Sensor Signal Output - to PIN1
# Brown  Cable: 3.3V VCC

# Black  Cable: Mode Selection (Unimplemented)

# Buzzer is connected to PIN2

import machine, utime

LedOnboard = machine.Pin(25,machine.Pin.OUT) # Board's LED
ON = 1
OFF = 0

PiezoElectricSensor = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_DOWN)
Buzzer = machine.Pin(1, machine.Pin.OUT)

def PiezoElectricHandler(pin):
    print("ALERT: Intruder Detected at" + str(utime.localtime()))
    Buzzer.value(ON)

PiezoElectricSensor.irq(trigger=machine.Pin.IRQ_RISING, handler=PiezoElectricHandler)

while True:
    LedOnboard.value(ON)
    utime.sleep(1) # delay 1 sec
    LedOnboard.value(OFF)
    utime.sleep(1) # delay 1 sec
    Buzzer.value(OFF)
