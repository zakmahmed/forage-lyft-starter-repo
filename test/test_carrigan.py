import unittest


from tyres.carrigan import Carrigan


class TestCarrigan(unittest.TestCase):
    def test_tyre_should_be_serviced(self):
        self.test_array = [0.1, 0.2, 0.8, 0.9]
        self.tyre = Carrigan(self.test_array)

        self.assertTrue(self.tyre.needs_service())

    def test_tyre_should_not_be_serviced(self):
        self.test_array = [0.1, 0.2, 0.8, 0.8]
        self.tyre = Carrigan(self.test_array)

        self.assertFalse(self.tyre.needs_service())
