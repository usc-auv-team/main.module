from abc import ABC, abstractmethod
class Path(ABC):

    @abstractmethod
    def increment(self, amount):
        pass

    @property
    @abstractmethod
    def target(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def independent_variable(self):
        raise NotImplementedError
