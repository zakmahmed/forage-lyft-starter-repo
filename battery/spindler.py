from battery.battery import Battery
from dateutil import relativedelta


class Spindler(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        delta = relativedelta.relativedelta(
            self.current_date, self.last_service_date)
        return delta.years > 2
