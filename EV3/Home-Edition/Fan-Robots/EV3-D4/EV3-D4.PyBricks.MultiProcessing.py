#!/usr/bin/env pybricks-micropython


from multiprocessing import Process

from ev3_d4_pybricks import EV3D4


ev3_d4 = EV3D4()

Process(target=ev3_d4.color_sensor_loop).start()

Process(target=ev3_d4.touch_sensor_loop).start()

ev3_d4.main_switch_loop()
