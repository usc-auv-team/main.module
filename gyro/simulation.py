from ._abstract import Gyro
class Simulated(Gyro):
    def __init__(self, update_hz):
        super().__init__()
        self.elapsed_time = 1.0/update_hz

        self._yaw = 0.0


    @property
    def roll(self):
        return 0.0# TODO

    @property
    def pitch(self):
        return 0.0# TODO

    @property
    def yaw(self):
        return self._yaw

    def complete_loop_update(self, propulsion):
        # elapsed time should be shorter than elapsed time for propulsion
        self._yaw += self.elapsed_time*propulsion.angular_speed
