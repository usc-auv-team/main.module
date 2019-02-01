from ._abstract import Odometer
class Middleman(Odometer):
    def __init__(self):

        import sys
        version = sys.version_info[0]
        if version == 2: super(Middleman, self).__init__()# Python 2
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

    def callback(self, new_message):
        """value should be in meters"""
        self._x = new_message.vector.x# meters
        self._y = new_message.vector.y# meters
        self._z = new_message.vector.x# meters
