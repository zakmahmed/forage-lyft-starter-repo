from engine.sternman_engine import SternmanEngine
import unittest
from datetime import datetime


class TestSternman(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = True
        self.engine = SternmanEngine(last_service_date, warning_light_is_on)
        self.assertTrue(self.engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False
        self.engine = SternmanEngine(last_service_date, warning_light_is_on)
        self.assertFalse(self.engine.needs_service())
