class Visualizer(object):
    def __init__(self):
        import cv2
        self.cv2 = cv2
        from numpy import zeros

        self.counter = 0
        self.position_graph = zeros((800, 800, 3), dtype = 'uint8')

    def position(self, x, y, z, every = 100):
        if self.counter%every is 0:
            blue = 255 + 50*z# color represents depth
            self.cv2.circle(self.position_graph, (int(10*x), 800 - int(10*y)), 5, (blue, 255, 0), -1)
            self.cv2.imshow('position', self.position_graph)
            self.cv2.waitKey(1)

        self.counter += 1

simulating = True

if __name__ == '__main__':
    if simulating:
        from gyro.simulation import Simulated as Gyro
        from odometer.simulation import Simulated as Odometer
        from propulsion.simulation import Simulated as Propulsion
        from planning.s2018.test import TestB

        gyro = Gyro(30.0)
        odometer = Odometer(30.0)
        propulsion = Propulsion(gyro, 30.0)
        strategy = TestB(gyro, odometer)

        visualizer = Visualizer()

        while True:
            try:
                strategy.run(propulsion, [])

                print(odometer.position.xyz)
                visualizer.position(odometer.position.x, odometer.position.y, odometer.position.z)
            except KeyboardInterrupt:
                break

    else:
        from gyro.ros_gyro import ROS_Gyro as Gyro
        from odometer.ros_odometer import ROS_Odometer as Odometer
        from propulsion.robot2018 import Robot2018 as Propulsion
