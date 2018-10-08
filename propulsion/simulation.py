import sys
sys.path.append('..')

import math
from time import time

from angle import OneD
from ._abstract import Propulsion
class Simulated(Propulsion):#TODO need depth stuff somewhere in here

    MAX_SPEED = 0.5# meters per second
    MAX_ACCEL = 0.1# meters per second^2

    MAX_ANGULAR_SPEED = 10.0# degrees per second
    MAX_ANGULAR_ACCEL = 3.0# degrees per second^2

    def __init__(self, gyro, update_hz):
        self.gyro = gyro
        self.elapsed_time = 1.0/update_hz

        self.speed = 0.0
        self.speed_target = 0.0

        self.angular_speed = 0.0
        self.angular_speed_target = 0.0


    def set_speed(self, speed):
        self.speed_target = speed

    def set_spin(self, spin):
        self.angular_speed_target = spin

    def travel_towards(self, heading):
        return self.face(heading)

    def correct_for(self, error_vector, P = 0.05):
        target_yaw = OneD.convert_to_angle(error_vector.x, error_vector.y)

        if abs(self.travel_towards(target_yaw)) < 5.0:
            xy_magnitude = (error_vector.x**2 + error_vector.y**2)**0.5
            self.set_speed(xy_magnitude*P)# TODO could use PID for more realism

    def face(self, heading, P = 0.05):
        error = self.gyro.path_to([0.0, 0.0, heading])[2]
        self.set_spin(error*P)# TODO could use PID for more realism
        return error


    def complete_loop_update(self):
        """LINEAR SPEED"""
        error = self.speed_target - self.speed
        self.speed += self.elapsed_time*math.copysign(Simulated.MAX_ACCEL, error)

        if abs(self.speed) > Simulated.MAX_SPEED:
            self.speed = math.copysign(Simulated.MAX_SPEED, self.speed)

        """ANGULAR SPEED"""
        error = self.angular_speed_target - self.angular_speed
        self.angular_speed += self.elapsed_time*math.copysign(Simulated.MAX_ANGULAR_ACCEL, error)

        if abs(self.angular_speed) > Simulated.MAX_ANGULAR_SPEED:
            self.angular_speed = math.copysign(Simulated.MAX_ANGULAR_SPEED, self.angular_speed)
