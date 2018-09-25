from vector import Vector

from ._abstract import Path
class CubicSpline(Path):
    def __init__(self, p0, p1, p2, p3, start):
        self.p0 = p0
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.start = start

        self._independent_variable = 0.0
        self.xyz = self.p0

    def bezier_eqn(self, dimension):
        t = self._independent_variable
        # P(t) = ((1-t)^3)*P0 + 3*((1-t)^3)*t*P1 + 3*(1-t)*(t^2)*P2 + (t^3)*P3, 0 <= t <= 1
        return self.p0[dimension]*(1 - t)**3 + 3*self.p1[dimension]*t*(1 - t)**2 + 3*self.p2[dimension]*(1 - t)*t**2 + self.p3[dimension]*t**3

    def increment(self, amount):
        self._independent_variable += amount
        if self._independent_variable > 1.0: return False
        x = self.bezier_eqn(0)
        y = self.bezier_eqn(1)
        z = self.bezier_eqn(2)

        self.xyz = [x, y, z]

        super().increment(amount)
        return True

    @property
    def target(self):
        return Vector(self.xyz)

    @property
    def independent_variable(self):
        return self.start + self._independent_variable
