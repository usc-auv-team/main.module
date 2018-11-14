from ._abstract import Gyro
class ROS_Gyro(Gyro):
    def __init__(self):

        import sys
        version = sys.version_info[0]
        if version == 2: super(Simulated, self).__init__()# Python 2
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

    def callback_on_new_roll(self, value):
        """value should be in degrees"""
        self._roll = value

    def callback_on_new_pitch(self, value):
        """value should be in degrees"""
        self._pitch = value

    def callback_on_new_yaw(self, value):
        """value should be in degrees"""
        self._yaw = value
