import math

from ._abstract import Odometer
class Simulated(Odometer):
    def __init__(self, update_hz):
        super().__init__()
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
        direction = math.radians(gyro.yaw)
        speed_x = propulsion.speed*math.sin(direction)
        speed_y = propulsion.speed*math.cos(direction)

        self._x += self.elapsed_time*speed_x
        self._y += self.elapsed_time*speed_y
