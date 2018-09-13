import time
import sys 
sys.path.append('..')

from odometer import Simulated as odometer
from paths import bezier as bezier

#This file is intended to test the correction vector calculation in simulation
if __name__ == '__main__':
    p0 = [0,0,0]
    p1 = [10,10,10]
    p2 = [20,20,20]
    p3 = [30,30,30]
    start = 0
    ideal_path = bezier.Bezier(p0,p1,p2,p3,start)

    odometer_simulator = odometer()
    odometer_simulator.initiate_simulation(ideal_path)
    
    start_time = time.time()
    #do a 1 min simulation
    while (time.time() - start_time ) < 60:
        time.sleep(1)
        x = odometer_simulator.x
        y = odometer_simulator.y
        z = odometer_simulator.z
        print("time(s) %s x:%s y:%s z: %s" % (time.time() - start_time ,  x, y, z))
    #create an straight line using spline
   
        
