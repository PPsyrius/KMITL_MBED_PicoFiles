# Assignment 2.4: Maker Driver for Pi Pico
# Docu: https://th.cytron.io/p-maker-drive-simplifying-h-bridge-motor-driver-for-beginner

import machine, utime

M1A = machine.PWM(machine.Pin(0))
M1B = machine.PWM(machine.Pin(1))

M1A.freq(50) # 50Hz is the default frequency for most servos
M1B.freq(50)

while True:
    for i in range(0,65535): # Servo has 65536 resolution level
        M1A.duty_u16(i)
    for i in range(0,65535):
        M1B.duty_u16(i)