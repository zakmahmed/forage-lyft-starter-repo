from abc import ABC, abstractmethod
from engine.engine import Engine
from battery.battery import Battery
from tyres.tyres import Tyre


class Car(ABC):

    def __init__(self, engine: Engine, battery: Battery, tyre: Tyre):
        self.engine = engine
        self.battery = battery
        self.tyre = tyre

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service() or self.tyre.needs_service()
