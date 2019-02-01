from ._abstract import Gyro
class Middleman(Gyro):
    def __init__(self):

        import sys
        version = sys.version_info[0]
        if version == 2: super(Middleman, self).__init__()# Python 2
        else: super().__init__()# Python 3
        del sys

        self._roll, self._pitch, self._yaw = [0.0, 0.0, 0.0]

    @property
    def roll(self):
        return self._roll

    @property
    def pitch(self):
        return self._pitch

    @property
    def yaw(self):
        return self._yaw

    def callback(self, new_message):
        """value should be in degrees"""
        self._roll = new_message.vector.x# degrees
        self._pitch = new_message.vector.y# degrees
        self._yaw = new_message.vector.z# degrees
