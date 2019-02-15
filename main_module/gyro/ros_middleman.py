from ._abstract import Gyro
class Middleman(Gyro):
    def __init__(self):

        import sys
        version = sys.version_info[0]
        if version == 2: super(Middleman, self).__init__()# Python 2
        else: super().__init__()# Python 3
        del sys

        self._roll, self._pitch, self._yaw = [0.0, 0.0, 0.0]
        self.initialized = False

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
        if not self.initialized:
            self.set_tare([new_message.vector.x, new_message.vector.y, new_message.vector.z], False)
            self.initialized = True
        else:
            self._roll = new_message.vector.y# degrees
            self._pitch = new_message.vector.x# degrees
            self._yaw = new_message.vector.z# degrees
