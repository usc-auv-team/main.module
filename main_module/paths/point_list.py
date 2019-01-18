from main_module.vector import Vector
from math import ceil

from ._abstract import Path
class PointList(Path):#TODO is this really necessary? could really be done by just giving Leash a series of points
    def __init__(self, points, start):
        self.points = [Vector(point) for point in points]
        self.start = start

        self._independent_variable = 0.0
        self.xyz = self.points[0]

    def increment(self, amount):
        self._independent_variable += amount
        if self._independent_variable > len(self.points) - 1: return False

        target_point_index = int(ceil(self._independent_variable))
        target_point = self.points[target_point_index]
        passed_point = self.points[target_point_index - 1]

        current_segment = target_point - passed_point#TODO assumes vectors
        self.xyz = passed_point + (self._independent_variable%1.0)*current_segment#TODO assumes vectors
        return True

    @property
    def target(self):
        return Vector(self.xyz)

    @property
    def independent_variable(self):
        return self.start + self._independent_variable
