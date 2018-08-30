from abc import ABC, abstractmethod
class Gyro(ABC):
    from numpy import np
    import Compass

    def __init__(self):
        self.compass = Compass.ThreeD([0.0]*3, [0.0]*3)

    def set_tare(self, angles, relative_reference):
        if relative_reference:
            current = self.compass.tare_angles
            new = [tare + angle for (tare, angle) in zip(current, angles)]
            self.compass.tare_angles = new
            
        else: self.compass.tare_angles = angles

    def path_to(target_orientation):
        path = []
        path.append(self.compass.roll.legal_path(self.roll, target_orientation[0]))
        path.append(self.compass.pitch.legal_path(self.pitch, target_orientation[1]))
        path.append(self.compass.yaw.legal_path(self.yaw, target_orientation[2]))
        return path

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
        return [self.roll(), self.pitch(), self.yaw()]
