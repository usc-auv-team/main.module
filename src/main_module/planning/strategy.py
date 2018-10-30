from .leash import Leash
from .events import Events
from abc import ABC, abstractmethod
class Strategy(ABC):

    def __init__(self, gyro, odometer):
        self.gyro = gyro
        self.odometer = odometer

    def init(self):
        self.leash = self._get_leash()
        self.events = self._get_events()

    @abstractmethod
    def _get_leash(self):
        return Leash([], 0.0, 0.0)

    @abstractmethod
    def _get_events(self):
        return Events([], [])

    def run(self, propulsion, subsystems):
        self.events.check(self.leash.independent_variable)
        self.events.execute(propulsion, subsystems)

        self._stay_on_path(propulsion)

    def _stay_on_path(self, propulsion):
        self.leash.maintain_length(self.odometer.position)
        propulsion.correct_for(self.leash.target - self.odometer.position)

        # TODO some of these updates are specific to simulation
        self.gyro.complete_loop_update(propulsion)
        self.odometer.complete_loop_update(self.gyro, propulsion)
        propulsion.complete_loop_update()
