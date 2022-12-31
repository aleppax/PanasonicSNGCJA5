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
  
## **Status register**

The Panasonic SN-GCJA5 has a proprietary logic capable of monitoring the status of critical parts and compensating with software correction in order to maintain a certain level of performance during the lifetime (expected lifetime of 5 years at 25°C, 60%RH on continuous current). 

### Particle Detect status [bit5][bit4]
0. Normal status
1. Normal status (within -80% against initial value), with S/W correction
2. Abnormal (below -90% against initial value), loss of function
3. Abnormal (below -80% against initial value), with S/W correction

### LED operational status [bit3][bit2]
0. Normal status
1. Normal status (within -70% against initial LOP), with S/W correction
2. Abnormal (below -90% against initial LOP) or no LOP, loss of function
3. Abnormal (below -70% against initial LOP), with S/W correction

### PWM Fan operational status [bit1][bit0]
0. Normal status
1. Normal status (1,000rpm or more), with S/W correction
2. In initial calibration
3. Abnormal (below 1,000rpm), out of control

### Overall sensor status [bit7][bit6]
0. everything is fine, thanks, I appreciate your interest
1. Abnormal status for any one of Particle detect, LED, PWM statuses
2. Abnormal status for any two of Particle detect, LED, PWM statuses
3. Abnormal status for any three of Particle detect, LED, PWM statuses

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
