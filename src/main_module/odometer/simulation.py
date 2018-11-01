"""FINISHED"""
import math

from ._abstract import Odometer
class Simulated(Odometer):
    def __init__(self, update_hz):

        import sys
        version = sys.version_info[0]
        if version == 2: super(Simulated, self).__init__()# Python 2
        else: super().__init__()# Python 3
        del sys
        
        self.elapsed_time = 1.0/update_hz

        self._x, self._y, self._z = [0.0, 0.0, 0.0]

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def z(self):
        return self._z

    def complete_loop_update(self, gyro, propulsion):
        """
        Update x and y by integrating speed over small time interval
        Speed is obtained from simulated propulsion instance
        """
        direction = math.radians(gyro.yaw)
        # break speed into x and y components
        speed_x = propulsion.speed*math.sin(direction)
        speed_y = propulsion.speed*math.cos(direction)
        # integrate
        self._x += self.elapsed_time*speed_x
        self._y += self.elapsed_time*speed_y
        self._z += self.elapsed_time*propulsion.depth_speed
