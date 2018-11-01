"""FINISHED"""
import sys

try:
    # works when ROS manages path
    from .. import vector
except:
    # works when ROS isn't involved
    sys.path.append('..')
    import vector

from vector import Vector
del vector

version = sys.version_info[0]
if version == 2:
    from abc import ABCMeta, abstractmethod, abstractproperty
    superclass = object
elif version == 3:
    from abc import ABC, abstractmethod
    superclass = ABC
else:
    print('This version of Python is unsupported.')


def compatible_abstractproperty(function):
    if version == 2: return abstractproperty(function)
    elif version == 3: return property(abstractmethod(function))
    else: return function


class Odometer(superclass):
    """
    Child classes should be polled anytime we need to get the robot's position
    """
    if version == 2: __metaclass__ = ABCMeta

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

    @compatible_abstractproperty
    def x(self):
        """
        Extend to retrieve current x position from hardware, txt, or ROS
        """
        raise NotImplementedError

    @compatible_abstractproperty
    def y(self):
        """
        Extend to retrieve current y position from hardware, txt, or ROS
        """
        raise NotImplementedError

    @compatible_abstractproperty
    def z(self):
        """
        Extend to retrieve current z position from hardware, txt, or ROS
        """
        raise NotImplementedError

    @property
    def position(self):
        return Vector([self.x, self.y, self.z]) - self.origin
