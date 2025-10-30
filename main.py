from car import RentCar
from rented_car import RentedCar
from user import Users
from arxiv import Arxiv

class RentCarApp:
    def __init__(self):
        self.cars = RentCar()
        self.arxiv = []
    def menu(self):
        print("""
=== 🚘 AVTOMOBIL IJARASI TIZIMI ===
1. Ro‘yxatdan o‘tish
2. Tizimga kirish
3. Mashinalarni ko‘rish
4. Mashina qo‘shish
5. Mashina ijaraga olish
6. Mashinani qaytarish
7. Ijara tarixim
8. Tizimdan chiqish
9. Chiqish
        """)

    def log_in(self, users: Users):
        try:
            email = input("📧 Emailingizni kiriting: ")
            password = int(input("🔑 Parolni kiriting: "))
            for user in users.users:
                if user.email == email and user.password == password:
                    print(f"✅ Xush kelibsiz, {user.name}!")
                    return user
            print("❌ Email yoki parol noto‘g‘ri!")
        except ValueError:
            print("⚠️ Parol faqat raqamlardan iborat bo‘lishi kerak!")

    def add_arxiv(self,arxiv):
        self.arxiv.append(arxiv)

    def mashina_ijaraga_berish(self, current_user):
        try:
            self.cars.show_cars()
            model = input("Qaysi modelni ijaraga olmoqchisiz? : ")
            for car in self.cars.cars:
                if car.model.lower() == model.lower() and car.status:
                    days = int(input("⏱ Necha kun ijaraga olmoqchisiz? : "))
                    total = days * car.price
                    car.status = False
                    arxiv =  Arxiv(len(self.arxiv)+1,userId=current_user.id)
                    arxiv.add_rented_car(RentedCar(carId=car.id,day=days))
                    self.add_arxiv(arxiv)
                    print(f"✅ Siz {car.model} mashinasini {days} kunga oldingiz.")
                    print(f"💰 To‘lov: ${total}\n")
        except ValueError:
            print("⚠️ Iltimos, kunlar sonini faqat raqamda kiriting!")

    def mashinani_qaytarish(self):
        try:
            model = input("Qaysi modelni qaytarmoqchisiz? : ")
            for car in self.cars.cars:
                if car.model.lower() == model.lower():
                    car.status = True
                    print(f"🔙 {car.model} qaytarildi.")
                    return
            print("❌ Bunday model topilmadi.")

        except Exception as e:
            print(f"⚠️ Xatolik: {e}")

    def my_history(self, current_user):
        print(f"{current_user.name} ijaralar tarixi:")
        found = False
        for arxiv in self.arxiv:
            if arxiv.userId == current_user.id:
                for rented_car in arxiv.rentedCars:
                    car = next((c for c in self.cars.cars if c.id == rented_car.carId), None)
                    if car:
                        total = rented_car.day * car.price
                        print(f"{car.model} - {rented_car.day} kun - ${total}")
                        found = True
        if not found:
            print("❌ Sizda hali ijaralar yo‘q.")
        print()

    def run(self, users: Users):
        current_user = None
        while True:
            self.menu()
            try:
                n = int(input("Tanlang :: "))
            except ValueError:
                print("⚠️ Iltimos, raqam kiriting!")
                continue
            match n:
                case 1:
                    users.add_user()
                case 2:
                    current_user = self.log_in(users)
                case 3:
                    self.cars.show_cars()
                case 4:
                    if current_user.is_admin:
                         self.cars.mashina_qushish(current_user)
                    else:
                        print("Faqat admin qo'shib biladi!")
                case 5:
                    self.mashina_ijaraga_berish(current_user)
                case 6:
                    self.mashinani_qaytarish()
                case 7:
                    self.my_history(current_user)
                case 8:
                    print(f"👋 {current_user.name}, tizimdan chiqdingiz.")
                    current_user = None
                case 9:
                    print("👋 Dasturdan chiqildi.")
                    break

if __name__ == "__main__":
    app = RentCarApp()
    users = Users()
    app.run(users)