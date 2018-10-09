simulating = True

if __name__ == '__main__':


    if simulating:
        from gyro.simulation import Simulated as Gyro
        from odometer.simulation import Simulated as Odometer
        from propulsion.simulation import Simulated as Propulsion
        # optional import for visualizer
        import numpy as np
        import cv2
        display = np.zeros((800, 800, 3), dtype = 'uint8')
        counter = 0
        # end optional import

        gyro = Gyro(30.0)
        odometer = Odometer(30.0)
        propulsion = Propulsion(gyro, 30.0)

        from paths.cubic_spline import CubicSpline
        p0 = [0,0,0]#TODO because of current simulation constraints Z must stay 0
        p1 = [3,60,-1]
        p2 = [70,10,-2]
        p3 = [70,70,-3]
        ideal_path = CubicSpline(p0, p1, p2, p3, 0.0)

        from planning.leash import Leash
        leash = Leash([ideal_path], length = 1.0, growth_rate = 0.01)

        while True:
            try:

                leash.maintain_length(odometer.position)
                propulsion.correct_for(leash.target - odometer.position)
                # command line output
                print(odometer.position.xyz)
                # end command line output
                # visualizer output
                if counter%100 is 0:
                    cv2.circle(display, (int(10*leash.target.x), 800 - int(10*leash.target.y)), 10, (255, 127, 0), -1)
                    cv2.circle(display, (int(10*odometer.position.x), 800 - int(10*odometer.position.y)), 5, (0, 255, 255), -1)
                    cv2.imshow('path', display)
                    cv2.waitKey(1)
                counter += 1
                # end visualizer output

                gyro.complete_loop_update(propulsion)
                odometer.complete_loop_update(gyro, propulsion)
                propulsion.complete_loop_update()

            except KeyboardInterrupt:
                break

    else:
        from gyro.fromROS import FromROS as Gyro
        from odometer.fromROS import FromROS as Odometer
        from propulsion.robot2018 import Robot2018 as Propulsion
