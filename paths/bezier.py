from ._abstract import Path
class Bezier(Path):
    def __init__(self, p0, p1, p2, p3, start):
        self.p0 = p0
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.start = start

        self.xyz = self.p0

    def increment(self, amount):
        self._independent_variable += amount
        if self._independent_variable > 1.0: return False

        i = self._independent_variable
        # P(t) = ((1-t)^3)*P0 + 3*((1-t)^3)*t*P1 + 3*(1-t)*(t^2)*P2 + (t^3)*P3, 0 <= t <= 1
        x = self.p0[0]*(1 - i)**3 + 3*self.p1[0]*i*(1 - i)**2 + 3*self.p2[0]*(1 - i)*i**2 + self.p3[0]*i**3
        y = self.p0[1]*(1 - i)**3 + 3*self.p1[1]*i*(1 - i)**2 + 3*self.p2[1]*(1 - i)*i**2 + self.p3[1]*i**3
        z = self.p0[2]*(1 - i)**3 + 3*self.p1[2]*i*(1 - i)**2 + 3*self.p2[2]*(1 - i)*i**2 + self.p3[2]*i**3
        self.xyz = [x, y, z]

        super().increment(amount)
        return True

    @property
    def target(self):
        return self.xyz

    @property
    def independent_variable(self):
        return self.start + self._independent_variable
