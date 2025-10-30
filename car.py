class Car:
    def __init__(self, id: int, model: str, price: int, status: bool):
        self.id = id
        self.model = model
        self.price = price
        self.status = status

class RentCar:
    def __init__(self, filename="cars.txt"):
        self.filename = filename
        self.cars = self.load_cars()

    def load_cars(self):
        cars = []
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                for line in file:
                    parts = line.strip().split(",")
                    if len(parts) == 4:
                        id = int(parts[0])
                        model = parts[1]
                        price = int(parts[2])
                        status = parts[3].lower() == "true"
                        cars.append(Car(id, model, price, status))
        except FileNotFoundError:
            pass
        return cars
    
    def save_cars(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            for car in self.cars:
                file.write(f"{car.id},{car.model},{car.price},{car.status}\n")

    def add_car(self, car: Car):
        self.cars.append(car)
        self.save_cars()

    def show_cars(self):
        print("🚘 Mavjud mashinalar:")
        found = False
        for index, car in enumerate(self.cars):
            if car.status:
                print(f"{index + 1}. {car.model} - ${car.price}/day [✅ Available]")
                found = True
        if not found:
            print("❌ Hozircha mavjud mashina yo‘q.")

    def mashina_qushish(self, current_user):
        try:
            model = input("🚘 Mashina modelini kiriting: ")
            price = int(input("💰 Kunlik narx ($): "))
            car = Car(len(self.cars) + 1, model, price, True)
            self.cars.append(car)
            self.save_cars()
            print(f"✅ {model} tizimga muvaffaqiyatli qo‘shildi!")
        except Exception as er:
            print(f"Xatolik {er} !")

