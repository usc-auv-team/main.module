from abc import ABC, abstractmethod
class Subsystem(ABC):
    """
    Designed such that its implementations can be put into an array and easily passed around.
    Allows for command-based coding.
    """
    @abstractmethod
    def init(self):
        """
        Run when robot boots up
        """
        pass

    @abstractmethod
    def perform(self, action, extra_parameters):
        """
        action: a string designating what to do (example: "MOVE_ARM")
        extra_parameters: a list of numbers providing details (example: [32] degrees)

        NOTE: subclasses should have a staticmethod that returns an enum of possible action strings
        """
        pass

    @abstractmethod
    def complete_loop_update(self):
        """
        Run at the end of every control loop
        """
        pass
