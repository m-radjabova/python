from bank_accaunt import BankAccount
from bank_system import BankSystem

class BankApp:
    def __init__(self):
        self.bank = BankSystem()

    def menu(self):
        print('''
        1. Hisob ochish
        2. Hisobga kirish
        0. Chiqish
        ''')

    def bank_menu(self):
        print('''
        === Bank menyusi ===
        1. Balansni ko‘rish
        2. Pul qo‘shish
        3. Pul yechish
        4. Pul o‘tkazish
        0. Chiqish  
        ''')

    def add_balance(self, account):
        balance = float(input("To‘ldirmoqchi bo‘lgan summani kiriting :::: "))
        account.add_balance(balance)
        print(f"Sizga {balance} dollar qo‘shildi")
    
    def withdraw_balance(self, account):
        summa = float(input("Yechib olmoqchi bo‘lgan summani kiriting :::: "))
        if account.withdraw(summa):
            print(f"Sizdan {summa} dollar yechildi")
        else:
            print("Balansda yetarli mablag‘ yo‘q!")
    
    def send_money(self, account):
        account_number = int(input("account numberni kiriting ::: "))
        user_account = self.bank.find_account_by_account_number(account_number)
        summa = float(input(f"necha pul o'tkazmoqchisiz {user_account.owner_name}ga  :::: "))
        res = account.withdraw(summa)
        if res:
            user_account.add_balance(summa)
            print(f"Pulingiz {user_account.owner_name} ga ko'chirildi !")
        else:
            print("mablag' yetarli emas")
    
    
    def make_task(self, account):
        while True:
            self.bank_menu()
            n = int(input("tanlang ::::: "))
            match n:
                case 1:
                    print(f"Balansingiz {account.get_balance()} dollar")
                case 2:
                    self.add_balance(account)
                case 3:
                    self.withdraw_balance(account)
                case 4:
                    self.send_money(account)
                case 0:
                    break
                case _:
                    print("Bunday menu mavjud emas !")

    def hisob_ochish(self):
        name = input("Ismingizni kiriting :::: ")
        balance = float(input("Hisobni qanchaga to‘ldirmoqchisiz :::: "))
        pin_code = int(input("PIN kodni kiriting :::: "))
        account = BankAccount(
            n=len(self.bank.accounts) + 1,
            name=name,
            balance=balance,
            pin_code=pin_code
        )
        self.bank.add_account(account)
        print("Hisob muvaffaqiyatli yaratildi!")
    
    def hisobga_kirish(self):
        pin_code = int(input("Kirish uchun PIN kodni kiriting :::: "))
        account = self.bank.find_account_by_pincode(pin_code)
        if account:
            self.make_task(account)
        else:
            print("Bunday account topilmadi!")

    def run(self):
        command = {
            1: self.hisob_ochish,
            2: self.hisobga_kirish,
            0: lambda: print("Tizim yopildi!! Hayr.")
        }
    
        while True:
            self.menu()
            order_n = int(input("tanlang :::: "))
            res =  command.get(order_n,False)
            if not res:
                break
            res()

app = BankApp()
app.run()