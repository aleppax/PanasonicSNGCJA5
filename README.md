# Panasonic-SN-GCJA5

## **Introduction**

Micropython driver for Panasonic SN-GCJA5 particulate matter (PM) sensor. Tested on Raspberry Pico W<br>
Port from [sngcja5](https://github.com/dvsu/PanasonicSNGCJA5)

## **Wiring**

Panasonic SN-GCJA5 uses `JST SM05B-GHS-TB(LF)(SN)` connector and requires 3.3V and 5V for direct wiring. 
Fortunately, Raspberry Pi GPIOs are 3.3V by default and also supports dual power supply voltages, 3.3V and 5V. 
Please refer to sensor specification sheet and table below for wiring guide.  

| Sensor Connector Pin | Symbol | Recommended Voltage | Description | RPico Physical Pin | RPi I/O |
| :---: | :---: | :---: | :---: | :---: | :---: |
| Pin 1 | TX | 3.3V | UART TX *(unused if using I2C protocol)* | *not connected* | |
| Pin 2 | SDA | 3.3V | I2C Data | Pin 1 | GP0 (I2C0 SDA) |
| Pin 3 | SCL | 3.3V | I2C Clock | Pin 2 | GP1 (I2C0 SCL) |
| Pin 4 | GND | 0V | Ground | Pin 38 | Ground |
| Pin 5 | VDD | 5V | Power supply | Pin 40 | 5v Power |

More details about [Raspberry Pico pinout](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html)
  

## **Examples**

```micropython
from machine import Pin, I2C
from picosngcja5 import SNGCJA5


# If SDA and SCL are connected to I2C bus 0, then:
i2c = I2C(0, sda=Pin(0), scl=Pin(1))
pm_sensor = SNGCJA5(i2c)



# The get_measurement method returns a dictionary of all measurement value 
result = pm_sensor.get_measurement()

print(result)
'''
    Structure of result
[
    {
    'mass_density': {
        'pm10': <float>,
        'pm2.5': <float>,
        'pm1.0': <float>
        }, 
    'particle_count': {
        'pm1.0': <float>, 
        'pm10': <float>, 
        'pm7.5': <float>, 
        'pm2.5': <float>, 
        'pm5.0': <float>, 
        'pm0.5': <float>
        }
    }
]
'''

```

## **Dependencies and Installation Instructions**

copy the library in your project and import it

## **Limitation**

Currently, this driver only supports **I2C** protocol
