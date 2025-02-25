#!/usr/bin/env pybricks-micropython



from pybricks.parameters import Button, Stop

from track3r_pybricks import Track3r


class Track3rWithBiBladeSpinner(Track3r):
    def spin_blade_by_ir_beacon(
            self,
            speed: float = 1000   # deg/s
        ):
        if Button.BEACON in self.ir_sensor.buttons(channel=self.ir_beacon_channel):
            self.medium_motor.run(speed=speed)

        else:
            self.medium_motor.stop()

            
    def main(self, speed: float = 1000):
        while True:
            self.drive_once_by_ir_beacon(speed=speed)

            self.spin_blade_by_ir_beacon(speed=speed)

            
if __name__ == '__main__':
    TRACKER_WITH_BIBLADE_SPINNER = Track3rWithBiBladeSpinner()

    TRACKER_WITH_BIBLADE_SPINNER.main()
