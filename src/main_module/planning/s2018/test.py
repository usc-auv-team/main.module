import sys
sys.path.append('..')

from paths.cubic_spline import CubicSpline
from planning.strategy import *
class TestA(Strategy):

    def __init__(self, gyro, odometer):
        super().__init__(gyro, odometer)
        """
        use this space to set instance variables that
        get_leash or get_events may depend on

        also use this space to set odometer origin
        """
        # now ready to init
        super().init()

    def _get_leash(self):
        p0 = [0,0,0]
        p1 = [3,60,-1]
        p2 = [70,10,-2]
        p3 = [70,70,-3]
        path0 = CubicSpline(p0, p1, p2, p3, 0.0)
        p0 = [70,70,-3]
        p1 = [10,70,-2]
        p2 = [60,3,-1]
        p3 = [0,0,0]
        path1 = CubicSpline(p0, p1, p2, p3, 1.0)
        return Leash([path0, path1], 1.0, 0.01)

    def _get_events(self):
        return Events([], [])


class TestB(Strategy):
    def __init__(self, gyro, odometer):
        super().__init__(gyro, odometer)
        """
        use this space to set instance variables that
        get_leash or get_events may depend on
        also use this space to set odometer origin
        """
        # now ready to init
        super().init()

    def _get_leash(self):
        p0 = [0,0,0]
        p1 = [3,60,-1]
        p2 = [70,10,-2]
        p3 = [70,70,-3]
        path0 = CubicSpline(p0, p1, p2, p3, 0.0)
        p0 = [70,70,-3]
        p1 = [10,70,-2]
        p2 = [60,3,-1]
        p3 = [0,0,0]
        path1 = CubicSpline(p0, p1, p2, p3, 1.0)
        return Leash([path0, path1], 1.0, 0.01)

    def _get_events(self):
        return Events([TestB._say_hi], [0.5])

    @staticmethod
    def _say_hi(propulsion, subsystems):
        print('Running Event:')
        print('Hello!')
        print('')
