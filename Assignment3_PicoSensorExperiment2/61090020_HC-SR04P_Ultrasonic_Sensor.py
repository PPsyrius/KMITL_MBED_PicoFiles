# Assignment 3.2: HC-SR04P Ultrasonic Sensor for Pi Pico
# Docu: https://www.thaieasyelec.com/product/581/hc-sr04p-ultrasonic-sensor

import utime
from hcsr04 import HCSR04

sensor = HCSR04(trigger_pin=0, echo_pin=1, air_temp=25)

while True:
    try:
        distance_cm = sensor.distance_cm()
        distance_mm = sensor.distance_mm()
        print('Distance (cm/mm):', distance_cm, 'cm;\t', distance_mm, 'mm')
    except Exception as ex:
        print('ERROR getting distance:', ex)
    utime.sleep(2)