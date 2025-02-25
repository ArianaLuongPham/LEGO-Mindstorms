#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, InfraredSensor, ColorSensor
from pybricks.media.ev3dev import SoundFile
from pybricks.parameters import Button, Color, Direction, Port, Stop
from pybricks.tools import wait

from random import randint

# import sys
# sys.path.append('/home/robot')
from util.drive_util_pybricks import IRBeaconRemoteControlledTank


class Kraz3(IRBeaconRemoteControlledTank, EV3Brick):
    WHEEL_DIAMETER = 24
    AXLE_TRACK = 100

    def __init__(
            self,
            left_motor_port: Port = Port.C, right_motor_port: Port = Port.B,
            wiggle_motor_port: Port = Port.A,
            polarity: str = 'inversed',
            touch_sensor_port: Port = Port.S1,
            color_sensor_port: Port = Port.S3,
            ir_sensor_port: Port = Port.S4, ir_beacon_channel: int = 1,
            debug: bool = False):
        super().__init__(
            wheel_diameter=self.WHEEL_DIAMETER, axle_track=self.AXLE_TRACK,
            left_motor_port=left_motor_port, right_motor_port=right_motor_port,
            polarity=polarity,
            ir_sensor_port=ir_sensor_port, ir_beacon_channel=ir_beacon_channel,
            debug=debug)

        self.wiggle_motor = Motor(port=wiggle_motor_port,
                                  positive_direction=Direction.CLOCKWISE)

        self.touch_sensor = TouchSensor(port=touch_sensor_port)

        self.color_sensor = ColorSensor(port=color_sensor_port)

        self.ir_beacon_channel = ir_beacon_channel

    def kungfu_manoeuvre_if_touched_or_remote_controlled(self):
        """
        Kung-Fu manoeuvre via Touch Sensor and Remote Control of head and arms
        """
        if self.touch_sensor.pressed():
            self.speaker.play_file(file=SoundFile.KUNG_FU)

            self.wiggle_motor.run_angle(
                speed=500,
                rotation_angle=360,
                then=Stop.HOLD,
                wait=True)

        elif Button.BEACON in \
                self.ir_sensor.buttons(channel=self.ir_beacon_channel):
            self.wiggle_motor.run(speed=111)

        else:
            self.wiggle_motor.stop()

    def kungfu_manoeuvre_whenever_touched_or_remote_controlled(self):
        while True:
            self.kungfu_manoeuvre_if_touched_or_remote_controlled()

    def react_to_color(self):
        detected_color = self.color_sensor.color()

        if detected_color == Color.YELLOW:
            self.speaker.play_file(file=SoundFile.YELLOW)

            self.wiggle_motor.run_angle(
                speed=-860,
                rotation_angle=360,
                then=Stop.HOLD,
                wait=True)

            self.speaker.play_file(file=SoundFile.UH_OH)

            wait(500)

            self.speaker.play_file(file=SoundFile.SNEEZING)

            wait(500)

        elif detected_color == Color.RED:
            self.speaker.play_file(file=SoundFile.SHOUTING)

            for _ in range(randint(1, 6)):
                self.speaker.play_file(file=SoundFile.SMACK)

            self.light.on(color=Color.RED)

            self.wiggle_motor.run_angle(
                speed=170,
                rotation_angle=360,
                then=Stop.HOLD,
                wait=True)

            self.speaker.play_file(file=SoundFile.LEGO)
            self.speaker.play_file(file=SoundFile.MINDSTORMS)

            self.light.off()

        elif detected_color == Color.BROWN:
            self.speaker.play_file(file=SoundFile.BROWN)

            wait(1000)

            self.wiggle_motor.run_angle(
                speed=-200,
                rotation_angle=360,
                then=Stop.HOLD,
                wait=True)

            self.speaker.play_file(file=SoundFile.CRYING)

        elif detected_color == Color.GREEN:
            self.speaker.play_file(file=SoundFile.GREEN)

            self.wiggle_motor.run_angle(
                speed=-400,
                rotation_angle=360,
                then=Stop.HOLD,
                wait=True)

            self.speaker.play_file(file=SoundFile.YES)

            wait(1000)

        elif detected_color == Color.BLUE:
            self.speaker.play_file(file=SoundFile.BLUE)

            self.speaker.play_file(file=SoundFile.FANTASTIC)

            self.speaker.play_file(file=SoundFile.GOOD_JOB)

            self.wiggle_motor.run_angle(
                speed=750,
                rotation_angle=360,
                then=Stop.HOLD,
                wait=True)

            self.speaker.play_file(file=SoundFile.MAGIC_WAND)

    def keep_reacting_to_colors(self):
        while True:
            self.react_to_color()

    def main(self):
        while True:
            self.drive_once_by_ir_beacon()

            self.kungfu_manoeuvre_if_touched_or_remote_controlled()

            self.react_to_color()


if __name__ == '__main__':
    KRAZ3 = Kraz3()

    KRAZ3.main()
