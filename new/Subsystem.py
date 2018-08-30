from abc import ABC, abstractmethod
class Subsystem(ABC):
    """
    Designed such that its implementations can be put into an array and easily passed around.
    Allows for command-based coding.
    """
    @abstractmethod
    def init(self):
        pass

    @abstractmethod
    def perform(self, action, extra_parameters):
        pass

    @abstractmethod
    def complete_loop_update(self):
        pass
