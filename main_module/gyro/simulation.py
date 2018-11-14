"""FINISHED"""
from ._abstract import Gyro
class Simulated(Gyro):
    def __init__(self, update_hz):

        import sys
        version = sys.version_info[0]
        if version == 2: super(Simulated, self).__init__()# Python 2
        else: super().__init__()# Python 3
        del sys

        self.elapsed_time = 1.0/update_hz

        self._yaw = 0.0


    @property
    def roll(self):
        """
        Approximate roll as 0 since the robot shouldn't tilt too much
        """
        return 0.0

    @property
    def pitch(self):
        """
        Approximate pitch as 0 since the robot shouldn't tilt too much
        """
        return 0.0

    @property
    def yaw(self):
        return self._yaw

    def complete_loop_update(self, propulsion):
        """
        Update yaw by integrating angular speed over small time interval
        Angular speed is obtained from simulated propulsion instance
        """
        self._yaw += self.elapsed_time*propulsion.angular_speed
