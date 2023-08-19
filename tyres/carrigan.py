from tyres.tyres import Tyre


class Carrigan(Tyre):
    def __init__(self, sensor_array):
        self.sensor_array = sensor_array

    def needs_service(self):
        if 0.9 in self.sensor_array:
            return True
        return False
