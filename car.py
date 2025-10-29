class Car:
    def __init__(self, id: int, model: str, price: int, status: bool):
        self.id = id
        self.model = model
        self.price = price
        self.status = status

class RentCar:
    def __init__(self):
        self.cars = []

    def add_car(self, car: Car):
        self.cars.append(car)

    def show_cars(self):
        print("🚘 Mavjud mashinalar:")
        for index, car in enumerate(self.cars):
            if car.status:
                print(f"{index + 1}. {car.model} - ${car.price}/day [✅ Available]")

    def mashina_qushish(self, current_user):
        try:
            model = input("🚘 Mashina modelini kiriting: ")
            price = int(input("💰 Kunlik narx ($): "))
            car = Car(len(self.cars) + 1, model, price, True)
            self.cars.append(car)
            print(f"✅ {model} tizimga muvaffaqiyatli qo‘shildi!")
        except Exception as er:
            print(f"Xatolik {er} !")

