#!/usr/bin/env python3


from threading import Thread

from kraz3_rctank_ev3dev1 import Kraz3


KRAZ3 = Kraz3()

Thread(
    target=KRAZ3.kungfu_manoeuvre_whenever_touched_or_remote_controlled,
    daemon=True).start()

Thread(
    target=KRAZ3.react_to_color,
    daemon=True).start()

KRAZ3.main()
