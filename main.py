from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, \
    not_equal_to
import math

# Create your objects here.
hub = MSHub()

for i in range(0, 100): print(' \n')

# Write your program here.
hub.speaker.beep()

mp = MotorPair('A', 'B')
ds = DistanceSensor('D')

alarm_distance = 10
# cs.light_up_all(3) # set light parameter

import time


def is_obstacle():
    return (ds.get_distance_cm(True) or 100) < alarm_distance  # distance sensor in obstacles


def move_obstacle():
    while is_obstacle():
        pass
    cs = ColorSensor('F')
    print(cs.get_color())  # distance sensor out but color sensor still in


mp.start_tank(10, 10)
while True:
    if is_obstacle():
        # print(ds.get_distance_cm())
        start = time.ticks_ms()
        move_obstacle()
        end = time.ticks_ms()
        print((end - start) / 1000)
    else:
        pass

