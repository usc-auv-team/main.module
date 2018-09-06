class Vector(Object):
    def __init__(xyz):
        self.xyz = xyz

    # def __call__(self):
    #     return [self.x, self.y, self.z]

    def __sub__(self, other):
        return Vector(self.x - other[0], self.y - other[1], self.z - other[2])

    def __add__(self, other):
        return Vector(self.x + other[0], self.y + other[1], self.z + other[2])

    def __isub__(self, other):
        return Vector(self.x - other[0], self.y - other[1], self.z - other[2])

    def __iadd__(self, other):
        return Vector(self.x + other[0], self.y + other[1], self.z + other[2])

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
