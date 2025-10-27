from rented_car import RentedCar

class Arxiv:
    def __init__(self, id: int, userId: int):
        self.id = id
        self.userId = userId
        self.rentedCars = []

    def add_rented_car(self, rented_car: RentedCar):
        self.rentedCars.append(rented_car)
