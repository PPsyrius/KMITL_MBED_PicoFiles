# Assignment 3.1: DS18B20 Digital Temp Probe for Pi Pico
# Docu: https://components101.com/sensors/ds18b20-temperature-sensor

# Temperature Range: -55°C to +125°C; Accuracy: ±0.5°C
# Black  Cable: GND
# Yellow Cable: Connect to a I2C SDA port
# Red    Cable: 3.3/5V

import time
import machine
import onewire, ds18x20

temp_probe = ds18x20.DS18X20(onewire.OneWire( machine.Pin(0) ))
roms = temp_probe.scan() #scan for device bus

if roms[0]: # if found, print out the address for the first probe
    print('Device found, address: ', roms)
else:
    exit

while True:
    print('Temp:', end=' ')
    temp_probe.convert_temp() # wait at least 750ms before read value
    print(temp_probe.read_temp(roms[0]), end='\n')
    time.sleep(2)