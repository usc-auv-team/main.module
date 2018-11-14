from ._abstract import Odometer
class ROS_Odometer(Odometer):
    def __init__(self):

        import sys
        version = sys.version_info[0]
        if version == 2: super(Simulated, self).__init__()# Python 2
        else: super().__init__()# Python 3
        del sys

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

    def callback_on_new_roll(self, value):
        self._x = value

    def callback_on_new_pitch(self, value):
        self._y = value

    def callback_on_new_yaw(self, value):
        self._z = value
