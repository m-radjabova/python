# class Group:
#     def __init__(self, id, name):
#         self.__id = id
#         self.__name = name
#         self.students = []
#
#     def get_id(self):
#         return self.__id
#
#     def set_name(self, name):
#         if len(name) > 3:
#             self.__name = name
#         else:
#             print("Ism 3 dan katta bo'lishi kerak!")
#
#     def get_name(self):
#         return self.__name
#
#     def __show_students(self):
#         for student in self.students:
#             print(f"name -- {student.name}")
#
#     def add_student(self, name):
#         self.__show_students()
#         self.students.append(name)
#
#
# group = Group(1, "1kt-23")
# id = group.get_id()
#
# group.set_name("2kt-23")
# name = group.get_name()
#
# group.add_student()

# === Bank tizimi ===
# 1. Hisob ochish
# 2. Hisobga kirish
# 0. Chiqish

# 2. Hisobga kirish
# ismingnizni kiriting
# pin kodni kirtiting


# === Bank menyusi ===
# 1. Balansni ko‘rish
# 2. Pul qo‘shish
# 3. Pul yechish
# 4. Pul o‘tkazish
# 5. Chiqish.

# account_number — hisob raqami (unikal, avtomatik yaratiladi)
# owner_name — egasining ismi
# balance — balans (float, boshlang‘ich 0)
# pin_code — maxfiy kod (string)


import random


class BankAccount:
    def __init__(self, name, balance, pin_code):
        self.__account_number = random.randint(1, 65620632626262)
        self.__owner_name = name
        self.__balance = balance
        self.__pin_code = pin_code

    def get_owner_name(self):
        return self.__owner_name

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def add_balance(self, amount):
        self.__balance += amount

    def withdraw_balance(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Balansda yetarli mablag‘ yo‘q!")

    def check_pin(self, pin_code):
        return self.__pin_code == pin_code

class BankSystem:
    def __init__(self):
        self.accounts = []

        acc1 = BankAccount("Muslima", 120000, "muslima")
        acc2 = BankAccount("Mariya", 150000, "mariya")
        self.accounts.extend([acc1, acc2])

    def add_account(self):
        name = input("Ismingizni kiriting : ")
        balance = int(input("Balansingizni kiriting : "))
        pin_code = input("Pin codingizni kiriting : ")
        bank_account = BankAccount(name, balance, pin_code)
        self.accounts.append(bank_account)
        print(f"{name} - akkauntingiz muaffaqiyatli ochildi!! ")

    def get_account(self, name, pin_code):
        for account in self.accounts:
            if account.get_owner_name() == name and account.check_pin(pin_code):
                return account
        return False

    def show_accounts(self):
        for i, account in enumerate(self.accounts):
            print(f"{i+1}. owner-name: {account.get_owner_name()}, account-number: {account.get_account_number()}")

    def find_account_by_account_number(self,account_number):
        for account in self.accounts:
            if account.get_account_number() == account_number:
                return account
        return False

    def send_money(self):
        print("Pul o'tkazish uchun mavjud accauntlar.")
        self.show_accounts()
        account_number = int(input("Kimga pul o'tkazmoqchisiz account numberini kiriting :::  "))
        account = self.find_account_by_account_number(account_number)
        if account:
            amount = int(input(f"{account.get_owner_name()}ga qancha pul o'tkazmoqchisiz : "))
            account.add_balance(amount)
            print(f"{account.get_owner_name()}ga {amount} pul o'tkazildi.")
        else:
            print("Account topilmadi! ")

bank = BankSystem()

def main():
    while True:
        print("=== Bank tizimi ===")
        print("1. -- Hisob ochish")
        print("2. -- Hisobga kirish ")
        print("0. -- Chiqish")
        n = int(input("Tanlang: "))

        match n:
            case 1:
                bank.add_account()
            case 2:
                name = input("Ismingizni kiriting : ")
                pin_code = input("Pin kodingizni kiriting : ")
                account = bank.get_account(name, pin_code)
                if account:
                    print("Hisobga muaffaqiyatli kirdingiz!")
                    bank_menu(account)
                else:
                    print("Bunday akkaunt topilmadi!")
            case 0:
                print("Tizim yopildi!! Hayr. ")
                break


def bank_menu(account):
    while account:
        print("=== Bank menyusi ===")
        print("1. -- Balansni ko‘rish")
        print("2. -- Pul qo‘shish")
        print("3. -- Pul yechish")
        print("4. -- Pul o‘tkazish")
        print("5. -- Chiqish.")

        n = int(input("Tanlang : "))
        match n:
            case 1:
                print(f"sizning balansingiz : {account.get_balance()}")
            case 2:
                amount = int(input("qancha pul qo'shmoqchsiz ? "))
                account.add_balance(amount)
                print(f"sizga {amount} so'm pul qo'shildi!")
                print(f"hozirgi balansingiz {account.get_balance()} so'm.")
            case 3:
                n = int(input("qancha pul yechib olmoqchisiz ? "))
                account.withdraw_balance(n)
                print(f"sizdan {n} so'm pul yechib olindi!")
                print(f"hozirgi balansingiz {account.get_balance()} so'm.")
            case 4:
                bank.send_money()
            case 5:
                print("Tizim yopildi!! Hayr.")
                break

main()
