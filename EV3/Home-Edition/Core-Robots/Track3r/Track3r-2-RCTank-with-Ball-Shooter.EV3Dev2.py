#!/usr/bin/env python3


from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C

from track3r_rc_tank_ev3dev2 import Track3r


class Track3rWithBallShooter(Track3r):
    def __init__(
            self,
            left_motor_port: str = OUTPUT_B, right_motor_port: str = OUTPUT_C,
            medium_motor_port: str = OUTPUT_A):
        super().__init__(
            left_motor_port=left_motor_port, right_motor_port=right_motor_port,
            medium_motor_port=medium_motor_port)

        self.remote.on_channel1_beacon = self.fire_ball


    def fire_ball(self, state):
        if state:
            self.medium_motor.on_for_rotations(
                speed=1000,
                rotations=3,
                brake=True,
                block=True)


if __name__ == '__main__':
    TRACK3R_WITH_BALL_SHOOTER = Track3rWithBallShooter()

    TRACK3R_WITH_BALL_SHOOTER.main()
