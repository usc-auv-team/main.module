simulating = True

if __name__ == '__main__':
    from gyro import FromROS as gyro
    from odometer import FromROS as odometer
    from propulsion import Robot2018 as propulsion


    if simulating:
        from gyro.simulation import Simulated as Gyro
        from odometer.simulation import Simulated as Odometer
        from propulsion.simulation import Simulated as Propulsion

        gyro = Gyro(30.0)
        odometer = Odometer(30.0)
        propulsion = Propulsion(gyro, 30.0)

        from paths.cubic_spline import CubicSpline
        p0 = [0,0,0]#TODO because of current simulation constraints Z must stay 0
        p1 = [10,10,0]
        p2 = [20,20,0]
        p3 = [30,30,0]
        ideal_path = CubicSpline(p0, p1, p2, p3, 0.0)

        from planning.leash import Leash
        leash = Leash([ideal_path], length = 1.0, growth_rate = 0.1)

        while True:
            try:

                leash.maintain_length(odometer.position)
                propulsion.correct_for(leash.target - odometer.position)
                print(odometer.position.xyz)

                gyro.complete_loop_update(propulsion)
                odometer.complete_loop_update(gyro, propulsion)
                propulsion.complete_loop_update()

            except KeyboardInterrupt:
                break

    else:
        from gyro.fromROS import FromROS as Gyro
        from odometer.fromROS import FromROS as Odometer
        from propulsion.robot2018 import Robot2018 as Propulsion
