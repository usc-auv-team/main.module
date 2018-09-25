from abc import ABC, abstractmethod
class Propulsion(ABC):
    """
    A set of common methods which can be implemented for most propulsion systems
    Having them all abstract makes it easier to write reusable code
    """
    @abstractmethod
    def set_speed(self, speed):
        """
        Should control how fast the robot moves in the direction set by travelTowards(heading)
        speed: likely a positive percentage in the range [0, 1]
        """
        pass

    @abstractmethod
    def set_spin(self, spin):
        """
        Should control how fast the robot spins; positive being clockwise and negative being counterclockwise
        spin: likely a percentage in the range [-1, 1]
        """
        pass

    @abstractmethod
    def travel_towards(self, heading):
        """
        Should control the direction in which the robot moves
        If the system is set up such that the front must be facing the direction of travel,
        face(heading, maximumOutput) should be called before moving.
        heading: the desired direction of travel, designated in degrees
        """
        pass

    @abstractmethod
    def correct_for(self, error_vector):
        """
        Should correct for positional error using some combination of the other functions and PID
        This can usually be accomplished using just travelTowards(heading) and setSpeed(speed)
        error_direction: the direction in which the robot should travel to decrease the error, designated in degrees
        error_magnitude: some indication of the size of the error that can be fed into PID
        """
        pass

    @abstractmethod
    def face(self, heading):
        """
        Should adjust the direction in which the front of the robot points using PID
        heading: which direction the front should face, designated in degrees
        return error between desired orientation and actual orientation, designated in degrees
        """
        pass

    @abstractmethod
    def complete_loop_update(self):
        """
        If each of the above methods were to send commands to the motors right away, propulsion behavior would be incredibly messy and limited.
        To achieve smoothness, information gathered from each method must be combined.
        For example, it must be given a heading from travel_towards(), a speed from set_speed(), and a spin from set_spin() before doing holonomic computations

        This function satisfies that requirement. It should be called at the end of each loop to coordinate the drivetrain's abilities, matching
        the caller's desired heading, speed, spin, etc. as closely as possible.
        """
        pass
