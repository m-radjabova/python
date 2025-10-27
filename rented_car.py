import datetime as dt

class RentedCar:
    def __init__(self, id: int, carId: int, day: int, date=None):
        self.id = id
        self.carId = carId
        self.day = day
        self.date = date or dt.datetime.today()
