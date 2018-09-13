"""FINISHED"""
import sys
sys.path.append('..')

from vector import Vector
from abc import ABC, abstractmethod
class Odometer(ABC):
    """
    Child classes should be polled anytime we need to get the robot's position
    """

    def __init__(self):
        self.origin = Vector([0]*3)

    def set_origin(self, xyz, relative_reference):
        """
        Sets the origins for x, y, and z

        xyz: [x, y, z] in same units as source data
        relative_reference: if false, replaces the current origin; if true, adds onto origin

        @Author Hayden Shively
        """
        if relative_reference: self.origin += xyz
        else:
            if type(xyz) is list: self.origin = Vector(xyz)
            else: self.origin = xyz

    def path_to(target_position):
        """
        Finds target_position - current position

        target_position: [x, y, z] in same units as source data
        return [x_difference, y_difference, z_difference] in same units as source data

        @Author Hayden Shively
        """
        return target_position - self.position

    @property
    @abstractmethod
    def x(self):
        """
        Extend to retrieve current x position from hardware, txt, or ROS
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def y(self):
        """
        Extend to retrieve current y position from hardware, txt, or ROS
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def z(self):
        """
        Extend to retrieve current z position from hardware, txt, or ROS
        """
        raise NotImplementedError

    @property
    def position(self):
        return Vector([self.x, self.y, self.z]) - self.origin
