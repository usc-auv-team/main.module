"""FINISHED"""
import sys
sys.path.append('..')

import math
from time import time

def clip(value, to):
    """
    Returns value if -to < value < to, else returns to with the sign of value

    @Author Hayden Shively
    """
    if abs(value) > to: return math.copysign(to, value)
    return value

from angle import OneD
from ._abstract import Propulsion
class Simulated(Propulsion):

    MAX_SPEED = 0.5# meters per second
    MAX_ACCEL = 0.1# meters per second^2

    MAX_ANGULAR_SPEED = 10.0# degrees per second
    MAX_ANGULAR_ACCEL = 3.0# degrees per second^2

    MAX_DEPTH_SPEED = 0.2# meters per second
    MAX_DEPTH_ACCEL = 0.01# meters per second^2

    def __init__(self, gyro, update_hz):
        self.gyro = gyro
        self.elapsed_time = 1.0/update_hz

        self.speed = 0.0
        self.speed_target = 0.0

        self.angular_speed = 0.0
        self.angular_speed_target = 0.0

        self.depth_speed = 0.0
        self.depth_speed_target = 0.0

    def set_speed(self, speed):
        """See comments in abstract"""
        self.speed_target = speed

    def set_spin(self, spin):
        """See comments in abstract"""
        self.angular_speed_target = spin

    def set_depth_speed(self, speed):
        """See comments in abstract"""
        self.depth_speed_target = speed

    def correct_for(self, error_vector, P = 0.05):
        """See comments in abstract"""
        self.set_depth_speed(error_vector.z*P)

        target_yaw = OneD.convert_to_angle(error_vector.x, error_vector.y)

        if abs(self.travel_towards(target_yaw)) < 5.0:
            xy_magnitude = (error_vector.x**2 + error_vector.y**2)**0.5
            self.set_speed(xy_magnitude*P)# could use full PID, but P is good enough

    def travel_towards(self, heading):
        """See comments in abstract"""
        return self.face(heading)

    def face(self, heading, P = 0.05):
        """See comments in abstract"""
        error = self.gyro.path_to([0.0, 0.0, heading])[2]
        self.set_spin(error*P)# could use full PID, but P is good enough
        return error


    def complete_loop_update(self):
        """See comments in abstract"""
        
        """LINEAR SPEED"""
        error = self.speed_target - self.speed
        self.speed += self.elapsed_time*math.copysign(Simulated.MAX_ACCEL, error)
        # clip to max value
        self.speed = clip(self.speed, to = Simulated.MAX_SPEED)

        """ANGULAR SPEED"""
        error = self.angular_speed_target - self.angular_speed
        self.angular_speed += self.elapsed_time*math.copysign(Simulated.MAX_ANGULAR_ACCEL, error)
        # clip to max value
        self.angular_speed = clip(self.angular_speed, to = Simulated.MAX_ANGULAR_SPEED)

        """DEPTH SPEED"""
        error = self.depth_speed_target - self.depth_speed
        self.depth_speed += self.elapsed_time*math.copysign(Simulated.MAX_DEPTH_ACCEL, error)
        # clip to max value
        self.depth_speed = clip(self.depth_speed, to = Simulated.MAX_DEPTH_SPEED)
