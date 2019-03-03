from ._abstract import Subsystem
class Vision(Subsystem):# TODO this must implement methods from superclass

    FOV_HORZ = 80
    FOV_VERT = 64
    WIDTH = 640
    HEIGHT = 480

    def __init__(self):

        import sys
        version = sys.version_info[0]
        if version == 2: super(Vision, self).__init__()# Python 2
        else: super().__init__()# Python 3
        del sys

        self.object_center = [0, 0]
        self.object_angle = [0, 0]

    def callback(self, new_message):
        data = json.loads(new_message.data)
        xmin = data['xmin']
        xmax = data['xmax']
        ymin = data['ymin']
        ymax = data['ymax']

        self.update_center(xmin, xmax, ymin, ymax)
        self.update_angle()

    def update_center(self, xmin, xmax, ymin, ymax):
        cx = (xmin + xmax)/2.0 - Vision.WIDTH/2.0
        cy = (ymin + ymax)/2.0 - Vision.HEIGHT/2.0
        self.object_center = [cx, cy]

    def update_angle(self):
        theta_horz = self.object_center[0]*Vision.FOV_HORZ/Vision.WIDTH
        theta_vert = self.object_center[1]*Vision.FOV_VERT/Vision.HEIGHT
        self.object_angle = [theta_horz, theta_vert]
