#!/usr/bin/env python3


from threading import Thread

from ev3_d4_rctank_ev3dev1 import EV3D4


ev3_d4 = EV3D4()

Thread(
    target=ev3_d4.color_sensor_loop,
    daemon=True).start()

Thread(
    target=ev3_d4.touch_sensor_loop,
    daemon=True).start()

ev3_d4.main()
