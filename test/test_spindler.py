import unittest
from datetime import datetime

from battery.spindler import Spindler


class TestSpindler(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)

        self.battery = Spindler(last_service_date, today)
        self.assertTrue(self.battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        self.battery = Spindler(last_service_date, today)
        self.assertFalse(self.battery.needs_service())
