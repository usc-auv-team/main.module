class Vector(Object):
    def __init__(xyz):
        self.x = xyz[0]
        self.y = xyz[1]
        self.z = xyz[2]

    def __call__(self):
        return [self.x, self.y, self.z]

    def __sub__(self, other):
        # [this - that for this, that in zip(self(), other())]
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
