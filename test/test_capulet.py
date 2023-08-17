from engine.capulet_engine import CapuletEngine
import unittest
from datetime import datetime


class TestCapulet(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        self.engine = CapuletEngine(
            last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(self.engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 2999
        last_service_mileage = 0

        self.engine = CapuletEngine(
            last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(self.engine.needs_service())
