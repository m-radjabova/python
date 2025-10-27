from car import RentCar
from user import Users

class RentCarApp:
    def __init__(self):
        self.cars = RentCar()

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

    def mashina_ijaraga_berish(self, current_user):
        try:
            self.cars.show_cars()
            model = input("Qaysi modelni ijaraga olmoqchisiz? : ")
            for car in self.cars.cars:
                if car.model.lower() == model.lower() and car.status:
                    if car.owner_id == current_user.id:
                        print("⚠️ Siz o‘zingiz qo‘shgan mashinani ijaraga ololmaysiz!")
                    days = int(input("⏱ Necha kun ijaraga olmoqchisiz? : "))
                    total = days * car.price
                    car.status = False

                    print(f"✅ Siz {car.model} mashinasini {days} kunga oldingiz.")
                    print(f"💰 To‘lov: ${total}\n")
        except ValueError:
            print("⚠️ Iltimos, kunlar sonini faqat raqamda kiriting!\n")

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
                    self.cars.mashina_qushish(current_user)
                case 5:
                    self.mashina_ijaraga_berish(current_user)
                case 6:
                    self.mashinani_qaytarish()
                case 8:
                    print(f"👋 {current_user.name}, tizimdan chiqdingiz.\n")
                    current_user = None
                case 9:
                    print("👋 Dasturdan chiqildi.")
                    break

if __name__ == "__main__":
    app = RentCarApp()
    users = Users()
    app.run(users)