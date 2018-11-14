from ._abstract import Odometer
class Disconnected(Odometer):
    def __init__(self):
        super().__init__()

    @property
    def x(self):
        return 0.0

    @property
    def y(self):
        return 0.0

    @property
    def z(self):
        return 0.0
