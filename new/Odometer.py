from abc import ABC, abstractmethod
class Odometer(ABC):
    import Vector

    def __init__(self):
        self.origin = ([0]*3)

    def set_origin(self, coords, relative_reference):
        if relative_reference:
            current = self.compass.tare_angles
            new = [old + increment for (old, increment) in zip(current, angles)]
            self.compass.tare_angles = new

        else: self.compass.tare_angles = angles

    def path_to(target_orientation):
        return self.compass.legal_path(self.orientation, target_orientation)

    @property
    @abstractmethod
    def roll(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def pitch(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def yaw(self):
        raise NotImplementedError

    @property
    def orientation(self):
        return [self.roll, self.pitch, self.yaw]
