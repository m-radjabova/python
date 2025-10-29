import datetime as dt

class RentedCar:
    def __init__(self, carId: int, day: int):
        self.carId = carId
        self.day = day
        self.date = dt.datetime.now()

