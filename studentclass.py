# class Student:

#     def __init__(self, name, last_name, age):
#         self.name = name
#         self.last_name = last_name
#         self.age = age

#     def say_hello(self):
#         return f"Hello, my name is {self.name} {self.last_name}."

#     def get_details(self):
#         return f"Name: {self.name}, Last Name: {self.last_name}, Age: {self.age}"


# student1 = Student("Muslima", "Radjabova", 18)
# print(student1.say_hello())


# Televizor clasini yaratish
# Pult

# xususiyatlari
# is_on = Yoniq
# volume  = 40
# language = "o'zbek"
# is_muted  = True
# current_channel = 1
# kannalar ro'yhati ["uzbek","yoshlar","buxoro"]

#  methodlari

#  TV Yoqish 
#  TV O'chirish 

# yoqilgandan so'ng
# oldinga - next
# orqaga - prev
# ovozini baland qilish - volume up
# ovozini past qilish - volume down
# ovozni to'liq o'chirish
# kanal o'tkazish nomer orqali



class Controller:
    def __init__(self):
        self.is_on = False
        self.volume = 10
        self.language = "o'zbek"
        self.is_muted = False
        self.current_channel = 1
        self.channels = ["Milliy TV", "Sevimli", "MY5"]

    def turn_on(self):
        self.is_on = True
        print("📺 Televizor yondi")

    def turn_off(self):
        self.is_on = False
        print("💤 Televizor o'chdi") 

    def volume_up(self):
        if self.volume < 100:
            self.volume += 1
            print(f"🔊 Ovoz balandlashdi: {self.volume}")
        else:
            print("⚠️ Ovoz eng yuqori darajada!")

    def volume_down(self):
        if self.volume > 0:
            self.volume -= 1
            print(f"🔉 Ovoz pasaydi: {self.volume}")
        else:
            print("⚠️ Ovoz eng past darajada!")

    def next_channel(self):
        self.current_channel += 1
        if self.current_channel > len(self.channels):
            self.current_channel = 1
        self.show_channel_name()

    def prev_channel(self):
        self.current_channel -= 1
        if self.current_channel < 1:
            self.current_channel = len(self.channels)
        self.show_channel_name()

    def show_channel_name(self):
        name = self.channels[self.current_channel - 1]
        print(f"📺 Hozirgi kanal: {name}")
    
    def volume_off(self):
        self.is_muted = True
        print("🔇 Ovoz o'chdi!")
    
    def volume_on(self):
        self.is_muted = False
        print("🔈 Ovoz yoqildi!")

    def set_channel_num(self, n):
        if 1 <= n <= len(self.channels):
            self.current_channel = n
            self.show_channel_name()
        else:
            print("❌ Bunday kanal mavjud emas!")
    
    def change_language(self):
        if self.language == "o'zbek":
            self.language = "rus" 
        else:
            self.language = "o'zbek"
        print(f"🌐 Til o'zgardi: {self.language}")


pult = Controller()

def main():
    print("1 — TV ni yoqish")
    print("2 — TV ni o'chirish")
    n = int(input("Tanlang: "))

    match n:
        case 1:
            pult.turn_on()
            show_commands()
        case 2:
            pult.turn_off()
        case _:
            print("❌ Noto‘g‘ri tugma bosildi!")

        
def show_commands():
    while pult.is_on:
        print("1 — Next kanal")
        print("2 — Prev kanal")
        print("3 — Volume up")
        print("4 — Volume down")
        print("5 — Ovoz o'chirish (mute)")
        print("6 — Ovoz yoqish (unmute)")
        print("7 — Kanalni raqam bilan tanlash")
        print("8 — Tilini o'zgartirish")
        print("9 — Televizorni o'chirish")
        command = int(input("Buyruqni tanlang: "))

        match command:
            case 1:
                pult.next_channel()
            case 2:
                pult.prev_channel()
            case 3:
                pult.volume_up()
            case 4:
                pult.volume_down()
            case 5:
                pult.volume_off()
            case 6:
                pult.volume_on()
            case 7:
                show_channels()
            case 8:
                pult.change_language()
            case 9:
                pult.turn_off()
            case _:
                print("❌ Noto‘g‘ri buyruq!")


def show_channels():
    print("\n📡 Mavjud kanallar:")
    for i, ch in enumerate(pult.channels, start=1):
        print(f"{i}. {ch}")

    n = int(input("Kanal raqamini kiriting: "))
    pult.set_channel_num(n)

main()
