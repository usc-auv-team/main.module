from abc import ABC, abstractmethod
class Odometer(ABC):
    """
    This class should be extended for a particular IMU or format of data in a text file.
    It should handle all the position data.
    """
    import Vector

    def __init__(self):
        self.origin = Vector([0]*3)

    def set_origin(self, xyz, relative_reference):
        if relative_reference: self.origin += xyz
        else:
            if type(xyz) is list: self.origin = Vector(xyz)
            else: self.origin = xyz

    def path_to(target_position):
        return target_position - self.position

    @property
    @abstractmethod
    def x(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def y(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def z(self):
        raise NotImplementedError

    @property
    def position(self):
        return Vector([self.x, self.y, self.z]) - self.origin
