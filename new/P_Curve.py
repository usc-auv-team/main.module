import Path
class P_Curve(Path):
    def __init__(self, xyz_lambda_function, start, end):
        self.function = vector_valued_function
        self.independent_variable = start
        self.end = end

    def increment(self, amount):
        self.independent_variable += amount
        super().increment(amount)
        return self.independent_variable < self.end

    @property
    def target(self):
        return self.function(self.independent_variable)


"""
format:
lambda t: [x(t), y(t), z(t)]

example:
lambda t: [at + b, ct + d, et + f]
"""
