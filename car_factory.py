from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

from battery.nubbin import Nubbin
from battery.spindler import Spindler

from tyres.carrigan import Carrigan
from tyres.octoprime import Octoprime

from car import Car


class CarFactory:

    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage, sensory_array):
        self.engine = CapuletEngine(
            last_service_date, current_mileage, last_service_mileage)
        self.battery = Spindler(last_service_date, current_date)
        self.tyre = Carrigan(sensory_array)

        return Car(self.engine, self.battery, self.tyre)

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage, sensory_array):
        self.engine = WilloughbyEngine(
            last_service_date, current_mileage, last_service_mileage)
        self.battery = Spindler(last_service_date, current_date)

        self.tyre = Carrigan(sensory_array)

        return Car(self.engine, self.battery, self.tyre)

    def create_palindrome(self, current_date, last_service_date, warning_light_on, sensory_array):
        self.engine = SternmanEngine(last_service_date, warning_light_on)
        self.battery = Spindler(last_service_date, current_date)

        self.tyre = Octoprime(sensory_array)

        return Car(self.engine, self.battery, self.tyre)

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage, sensory_array):
        self.engine = WilloughbyEngine(
            last_service_date, current_mileage, last_service_mileage)
        self.battery = Nubbin(last_service_date, current_date)

        self.tyre = Octoprime(sensory_array)

        return Car(self.engine, self.battery, self.tyre)

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage, sensory_array):
        self.engine = CapuletEngine(
            last_service_date, current_mileage, last_service_mileage)
        self.battery = Nubbin(last_service_date, current_date)

        self.tyre = Carrigan(sensory_array)

        return Car(self.engine, self.battery, self.tyre)
