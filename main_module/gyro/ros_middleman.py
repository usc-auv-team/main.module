from ._abstract import Gyro
class Middleman(Gyro):

    LOOKUP = {'roll':0, 'pitch':1, 'yaw':2}

    def __init__(self):

        import sys
        version = sys.version_info[0]
        if version == 2: super(Middleman, self).__init__()# Python 2
        else: super().__init__()# Python 3
        del sys

        self._roll, self._pitch, self._yaw = [0.0, 0.0, 0.0]
        self._initialized = False

        self._roll_source = 'x'
        self._pitch_source = 'y'
        self._yaw_source = 'z'

    @property
    def roll(self):
        return self._roll - self.angle.tare_angles[0]
    @property
    def pitch(self):
        return self._pitch - self.angle.tare_angles[1]
    @property
    def yaw(self):
        return self._yaw - self.angle.tare_angles[2]

    def callback(self, new_message):
        """values should be in degrees"""
        # self._roll = new_message.vector.y# degrees
        # self._pitch = new_message.vector.x# degrees
        # self._yaw = new_message.vector.z# degrees

        vector = new_message.vector.__dict__

        self._roll = vector[self._roll_source]# degrees
        self._pitch = vector[self._pitch_source]# degrees
        self._yaw = vector[self._yaw_source]# degrees

        if not self._initialized:
            self.set_tare([vector[self._roll], vector[self._pitch], vector[self._yaw]], False)
            self._initialized = True


    def configure_message_outlets(self, x, y, z):
        """expects x, y, and z to be any of the following: 'roll', 'pitch', or 'yaw'"""
        temp = [0, 0, 0]
        temp[Middleman.LOOKUP[x]] = 'x'
        temp[Middleman.LOOKUP[y]] = 'y'
        temp[Middleman.LOOKUP[z]] = 'z'

        self._roll_source, self._pitch_source, self._yaw_source = temp
