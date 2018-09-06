"""FINISHED, with the exception of IEEE remainder stuff"""
from math import copysign, sqrt, log, atan2, degrees#, remainder TODO
from numpy import sin, cos, radians

def remainder(x, y):
    """
    This isn't an exact replica of the IEEE standard, but it's close enough for now.
    Python 3.7 has an actual implementation of this TODO: SWITCH
    """
    from math import ceil
    n = x/y
    # if round(n, 2)%1.0 == 0.5:
    #     n = ceil(x/y, 1)
    #     if n%2.0 != 0.0: n-=1
    # print(n)
    return x - round(n, 0)*y

class OneD(object):
    def __init__(self, protected_zone_start, protected_zone_size):
        """
        Angles increase as the numbers on a clock increase.

        protected_zone_start: the first protected angle encountered by a minute hand which starts at 12:00
        protected_zone_size: the number of degrees the minute hand must travel before reaching the end of the protected section

        @Author Hayden Shively
        """
        self.protected_zone_start = protected_zone_start
        self.protected_zone_size = abs(protected_zone_size)%360

        self.tare_angle = 0.0

    @staticmethod
    def validate(angle):# tested, works
        """
        Wraps values around a circle

        angle: degrees, can be positive, negative, huge, or tiny
        return the corresponding angle in the range [0, 360)

        @Author Hayden Shively
        """
        if angle < 0.0: temp = 360.0 - abs(angle)%360.0
        else: temp = angle%360.0

        return temp if temp < 360.0 else 0.0

    @staticmethod
    def path(start, end):# tested, works
        """
        Finds the measure of the minor arc between two points on a circle
        start: the first point, designated in degrees
        end: the second point, designated in degrees
        return arc measure in degrees (positive if the arc is clockwise of start, negative if it's counterclockwise of start)

        @Author Hayden Shively
        """
        return remainder(end - start, 360.0)

    def legalize(self, angle):# tested, works
        """
        Calls validate(angle) If the result is inside the protected zone,
        this method pushes it out to the nearest zone border.

        angle: degrees, can be positive, negative, huge, or tiny
        return the corresponding angle in the range [0, 360) \ (zone start, zone end)

        @Author Hayden Shively
        """
        if self.protected_zone_size != 0:
            from_starting_edge = Compass.path(self.protected_zone_start, angle)
            to_ending_edge = Compass.path(angle, self.protected_zone_end)

            if from_starting_edge < 0.0:
                from_starting_edge += 360.0
                from_starting_edge = copysign(from_starting_edge, to_ending_edge)

            if 0.0 < from_starting_edge and from_starting_edge < self.protected_zone_size:
                angle = self.protected_zone_start if from_starting_edge <= abs(to_ending_edge) else self.protected_zone_end

        return Compass.validate(angle)

    def border_path(self, start):# tested, works
        """
        Uses path(start, end) to find the minor arc measure between start and the nearest zone border

        start: degrees, can be positive, negative, huge, or tiny
        return arc measure in degrees (positive if the arc is clockwise of start, negative if it's counterclockwise of start)

        @Author Hayden Shively
        """
        to_starting_edge = Compass.path(start, self.protected_zone_start)
        to_ending_edge = Compass.path(start, self.protected_zone_end)

        return to_starting_edge if abs(to_starting_edge) <= abs(to_ending_edge) else to_ending_edge

    def legal_path(self, start, end):# tested, works
        """
        Uses path(start, end) to find the smallest arc between start and legalize(end) that
        doesn't intersect the protected zone. If start was in that zone, borderPath(start) is added to the result

        start: the first point, designated in degrees
        end: the second point, designated in degrees
        return arc measure in degrees (positive if the arc is clockwise of start, negative if it's counterclockwise of start)

        @Author Hayden Shively
        """
        start_legal = self.legalize(start)
        path_escape = 0.0 if Compass.validate(start) == start_legal else self.border_path(start)
        path_main = Compass.path(start_legal, self.legalize(end))

        if self.protected_zone_size != 0:
            path_border = self.border_path(start_legal)

            comparator = 0 if path_border == 0 else 1
            if path_border == 0: path_border = Compass.path(start_legal, self.protected_zone_start + self.protected_zone_size/2.0)
            if path_main/path_border > comparator: path_main -= copysign(360.0, path_main)

        return path_main + path_escape

    @staticmethod
    def stdd(angles):# tested, works
        """
        Calculates the standard deviation of an ndarray of angles (can handle 360->0 boundary condition)

        angles: an array of angles in degrees
        return the standard deviation in degrees

        @Author Hayden Shively
        """
        sins = sin(radians(angles))
        coss = cos(radians(angles))
        sins_sum = sins.sum() / angles.shape[0]
        coss_sum = coss.sum() / angles.shape[0]

        stdd = sqrt(-log(sins_sum*sins_sum + coss_sum*coss_sum))
        return degrees(stdd)

    @staticmethod
    def convert_to_angle(x, y):# tested, works
        """
        x: x coordinate
        y: y coordinate
        return the angle between the Y axis and (x, y) measured in degrees
        
        @Author Hayden Shively
        """
        return degrees(atan2(x, -y))

    @property
    def protected_zone_end(self):# tested, works
        return self.protected_zone_start + self.protected_zone_size

class ThreeD(object):
    def __init__(self, protected_zone_starts, protected_zone_sizes):
        self.roll = OneD(protected_zone_starts[0], protected_zone_sizes[0])
        self.pitch = OneD(protected_zone_starts[1], protected_zone_sizes[1])
        self.yaw = OneD(protected_zone_starts[2], protected_zone_sizes[2])

    @property
    def tare_angles(self):
        return [self.roll.tare_angle, self.pitch.tare_angle, self.yaw.tare_angle]

    @tare_angles.setter
    def tare_angles(self, angles):
        self.roll.tare_angle = angles[0]
        self.pitch.tare_angle = angles[1]
        self.yaw.tare_angle = angles[2]

    def legal_path(self, starts, ends):
        return [self.roll.legal_path(start[0], end[0]), self.pitch.legal_path(start[1], end[1]), self.yaw.legal_path(start[2], end[2])]
