import sys
sys.path.append('..')

from main_module.paths.cubic_spline import CubicSpline
from main_module.planning.strategy import *
class TestA(Strategy):

    name = 'Skewed Figure-Eight'

    def __init__(self, gyro, odometer):
        import sys
        version = sys.version_info[0]
        if version == 2: super(TestA, self).__init__(gyro, odometer)# Python 2
        else: super().__init__(gyro, odometer)# Python 3
        del sys
        """
        use this space to set instance variables that
        get_leash or get_events may depend on

        also use this space to set odometer origin
        """
        # now ready to init
        self.init()

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

    name = 'Skewed Figure-Eight with Events'

    def __init__(self, gyro, odometer):
        import sys
        version = sys.version_info[0]
        if version == 2: super(TestB, self).__init__(gyro, odometer)# Python 2
        else: super().__init__(gyro, odometer)# Python 3
        del sys
        """
        use this space to set instance variables that
        get_leash or get_events may depend on

        also use this space to set odometer origin
        """
        # now ready to init
        self.init()

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
        return Events([TestB._say_hi, TestB._say_goodbye], [0.5, 1.5])

    @staticmethod
    def _say_hi(propulsion, subsystems, call_count):
        if call_count is 0:
            print('Running Event:')
            print('Hello!')
            print('')

    @staticmethod
    def _say_goodbye(propulsion, subsystems, call_count):
        if call_count is 0:
            print('Running Event:')
            print('Goodbye!')
            print('')
