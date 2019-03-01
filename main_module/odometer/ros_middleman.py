from ._abstract import Odometer
class Middleman(Odometer):

    LOOKUP = {'east':0, '-east':0, 'pitch':1, '-pitch':1, 'yaw':2, '-yaw':2}

    def __init__(self):

        import sys
        version = sys.version_info[0]
        if version == 2: super(Middleman, self).__init__()# Python 2
        else: super().__init__()# Python 3
        del sys

        self._x, self._y, self._z = [0.0, 0.0, 0.0]

        self._x_source = (1.0, 'x')
        self._y_source = (1.0, 'y')
        self._z_source = (1.0, 'z')

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
        """values should be in meters"""
        # self._x = -new_message.vector.x# meters
        # self._y = new_message.vector.y# meters
        # self._z = new_message.vector.x# meters
        vector = new_message.vector.__dict__

        self._x = self._x_source[0]*vector[self._x_source[1]]# meters
        self._y = self._y_source[0]*vector[self._y_source[1]]# meters
        self._z = self._z_source[0]*vector[self._z_source[1]]# meters

    def configure_message_outlets(self, x, y, z):
        """
        expects x, y, and z to be any of the following:
        'east' or '-east'
        'north' or '-north'
        'down' or '-down'
        """
        signs = [-1.0 if '-' in str else 1.0 for str in [x, y, z]]
        temp = [0, 0, 0]
        temp[Middleman.LOOKUP[x]] = 'x'
        temp[Middleman.LOOKUP[y]] = 'y'
        temp[Middleman.LOOKUP[z]] = 'z'

        self._x_source, self._y_source, self._z_source = zip(signs, temp)
