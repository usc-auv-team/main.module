from _abstract import Path
class Curve(Path):
    def __init__(self, xyz_lambda_function, start, end):
        self.function = xyz_lambda_function
        self._independent_variable = start
        self.end = end

    def increment(self, amount):
        self._independent_variable += amount
        super().increment(amount)
        return self._independent_variable < self.end

    @property
    def target(self):
        return self.function(self._independent_variable)

    @property
    def independent_variable(self):
        return self._independent_variable


"""
format:
lambda t: [x(t), y(t), z(t)]

usage example:
my_func = lambda t: [t, t**2, t**3]
my_curve = P_Curve(my_func, 0.0, 3.0)

while my_curve.increment(0.5):
    print(my_curve.target)

"""
