import sys
sys.path.append('..')

from main_module.paths.point_list import PointList
from ..strategy import *
class TestA(Strategy):

    name = 'Triangle'

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
        p1 = [0.75,0.75,-0.5]
        p2 = [-0.75,0.75,-0.5]
        path0 = PointList([p0, p1, p2, p0], 0.0)
        return Leash([path0], 0.05, 0.005)

    def _get_events(self):
        return Events([], [])

from math import sin, cos, radians
class FollowVision(Strategy):

    name = 'Follow Computer Vision'

    def __init__(self, gyro, odometer):
        import sys
        version = sys.version_info[0]
        if version == 2: super(FollowVision, self).__init__(gyro, odometer)# Python 2
        else: super().__init__(gyro, odometer)# Python 3
        del sys
        """
        use this space to set instance variables that
        get_leash or get_events may depend on

        also use this space to set odometer origin
        """
        self.vision_target = [0, 0, 0]
        # now ready to init
        self.init()

    def _get_leash(self):
        p0 = self.vision_target
        path0 = PointList([p0], 0.0)
        return Leash([path0], 0.05, 0.005)

    def _get_events(self):
        return Events([FollowVision._update_target], [0.0])

    def _update_target(propulsion, subsystems, call_count):
        vision = subsystems[0]
        theta = radians(vision.object_angle[0])
        self.vision_target[0] = 2.0*sin(theta)
        self.vision_target[1] = 2.0*cos(theta)

        self.leash = self._get_leash()

from main_module.paths.cubic_spline import CubicSpline
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
        p1 = [0.06,1.2,-0.25]
        p2 = [1.4,0.2,-0.5]
        p3 = [1.4,1.4,-0.75]
        path0 = CubicSpline(p0, p1, p2, p3, 0.0)
        path1 = CubicSpline(p3, p1, p2, p0, 1.0)
        return Leash([path0, path1], 0.05, 0.005)

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

from main_module.paths.curve import Curve
class SinWave(Strategy):

    name = 'sin wave'

    def __init__(self, gyro, odometer):
        import sys
        version = sys.version_info[0]
        if version == 2: super(SinWave, self).__init__(gyro, odometer)# Python 2
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
        my_lambda = lambda t: [0.5*sin(t), 0.25*t, -0.10*t]
        path0 = Curve(my_lambda, 0.0, 2*3.1415)
        return Leash([path0], 0.05, 0.005)

    def _get_events(self):
        return Events([], [])
