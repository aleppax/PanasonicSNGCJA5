from machine import Pin, I2C
from picosngcja5 import SNGCJA5


# If SDA and SCL are connected to I2C bus 0, then:
i2c = I2C(0, sda=Pin(0), scl=Pin(1))
pm_sensor = SNGCJA5(i2c)

# get oldest measurement from queue
single_measure = pm_sensor.get_measurement()

# empty_measurements_queue
pm_sensor.empty_measurements_queue()

# acquire 3 measurements
print(pm_sensor.measurements_serie(3))
