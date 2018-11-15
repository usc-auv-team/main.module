"""FINISHED"""
class Vector(object):
    """
    A simple class to add and subtract 3 element vectors. Easily modified to handle longer vectors.

    @Author Hayden Shively
    """
    def __init__(self, xyz):
        self.xyz = xyz

    def __call__(self):
        return self.xyz

    def __mul__(self, other):
        return Vector([self.x*other, self.y*other, self.z*other])

    def __imul__(self, other):
        return Vector([self.x*other, self.y*other, self.z*other])

    __rmul__ = __mul__

    def __sub__(self, other):
        return Vector([self.x - other[0], self.y - other[1], self.z - other[2]])

    def __add__(self, other):
        return Vector([self.x + other[0], self.y + other[1], self.z + other[2]])

    def __isub__(self, other):
        return Vector([self.x - other[0], self.y - other[1], self.z - other[2]])

    def __iadd__(self, other):
        return Vector([self.x + other[0], self.y + other[1], self.z + other[2]])

    def __getitem__(self, key):
        return self.xyz[key]

    @property
    def x(self):
        return self[0]

    @property
    def y(self):
        return self[1]

    @property
    def z(self):
        return self[2]

    def magnitude(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5
