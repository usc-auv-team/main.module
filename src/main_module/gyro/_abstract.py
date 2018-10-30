"""FINISHED"""
#import sys
#sys.path.append('..')

from .. import angle
from abc import ABC, abstractmethod
class Gyro(ABC):
    """
    Child classes should be polled anytime we need to get the robot's orientation
    """

    def __init__(self):
        # creates a ThreeD angle class with no protected zones
        # (gyro is a sensor, not a mechanism with movement constraints)
        self.angle = angle.ThreeD([0.0]*3, [0.0]*3)

    def set_tare(self, angles, relative_reference):
        """
        Sets the angular "origins" for roll, pitch, and yaw

        angles: [roll_tare, pitch_tare, yaw_tare], specified in degrees
        relative_reference: if false, replaces the current tares; if true, adds onto them

        @Author Hayden Shively
        """
        if relative_reference:
            new = [old + increment for (old, increment) in zip(self.angle.tare_angles, angles)]
            self.angle.tare_angles = new

        else: self.angle.tare_angles = angles

    def path_to(self, target_orientation):
        """
        Finds shortest path from the current orientation to target_orientation

        target_orientation: [roll_target, pitch_target, yaw_target], specified in degrees
        return [roll_path, pitch_path, yaw_path], specified in degrees

        @Author Hayden Shively
        """
        return self.angle.legal_path(self.orientation, target_orientation)

    @property
    @abstractmethod
    def roll(self):
        """
        Extend to retrieve current roll from hardware, txt, or ROS
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def pitch(self):
        """
        Extend to retrieve current pitch from hardware, txt, or ROS
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def yaw(self):
        """
        Extend to retrieve current yaw from hardware, txt, or ROS
        """
        raise NotImplementedError

    @property
    def orientation(self):
        return [self.roll, self.pitch, self.yaw]
