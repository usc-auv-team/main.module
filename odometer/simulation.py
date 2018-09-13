from ._abstract import Odometer
import timeit
import time

class Simulated(Odometer):
    def __init__(self):
        super().__init__()
        self.simulation_time = 1 #in minutes
        self.ideal_path = None
        self.type = type(self.ideal_path)
        self.simulated_path = {} # a dictionary with time (msec) as key, and value of [x,y,z]
        self.simulation_start_time = time.time()
        pass

    def __str__(self):
        return "%s %s %s" % (self.x,self.y,self.z)

    def get_current_time_msec(self):
        simulation_time = 1000* ( time.time() - self.simulation_start_time )
        return int(simulation_time)

    @property
    def x(self):
        return self.simulated_path[self.get_current_time_msec()][0]

    @property
    def y(self):
        return self.simulated_path[self.get_current_time_msec()][1]

    @property
    def z(self):
        return self.simulated_path[self.get_current_time_msec()][2]

    # takes a ideal path (bezier) and creates a noisy version and add a time intervals,
    # to simulate the actual current position in respect to time.
    def initiate_simulation(self, path):
        SIMULATION_TIME_MSEC = self.simulation_time * 60000 #5 minute in increments of 1 ms.
        #create a noise generation function as a function of time. 
        self.ideal_path = path
        simulated_data= {}
        for i in range(0,SIMULATION_TIME_MSEC):
            increment = 1.0/SIMULATION_TIME_MSEC
            self.ideal_path.increment(increment)
            simulated_data[i] =  self.shift_position( self.ideal_path.target )
        self.simulated_path = simulated_data
        
    #function to generate noise in data to test correction vector    
    #this first one simply shifts one dimension over by a number 
    def shift_position(self, xyz):
        xyz[0] += 10 #10 is randomly chosen number
        return xyz


