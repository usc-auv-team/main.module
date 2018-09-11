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
        x = p0[0]*(1 - i)**3 + 3*p1[0]*i*(1 - i)**2 + 3*p2[0]*(1 - i)*i**2 + p3[0]*i**3
        y = p0[1]*(1 - i)**3 + 3*p1[1]*i*(1 - i)**2 + 3*p2[1]*(1 - i)*i**2 + p3[1]*i**3
        z = p0[2]*(1 - i)**3 + 3*p1[2]*i*(1 - i)**2 + 3*p2[2]*(1 - i)*i**2 + p3[2]*i**3
        self.xyz = [x, y, z]

        super().increment(amount)
        return True

    @property
    def target(self):
        return self.xyz

    @property
    def independent_variable(self):
        return self.start + self._independent_variable
