from bank_accaunt import BankAccount
from bank_system import BankSystem

bank = BankSystem()

def menu():
    print('''
    1. Hisob ochish
    2. Hisobga kirish
    0. Chiqish
    ''')

def bank_menu():
    print('''
    === Bank menyusi ===
    1. Balansni ko‘rish
    2. Pul qo‘shish
    3. Pul yechish
    4. Pul o‘tkazish
    0. Chiqish.  
    ''')

def add_balance(account):
    balance = float(input("To'ldirmoqchi bo'lgan summani kiriting :::: "))
    account.add_balance(balance)
    print(f"sizga {balance} dollar qushildi")

def withdraw_balance(account):
    summa = float(input("Yechib olmoqchi bulgan summani kiriting :::: "))
    account.withdraw(summa)
    print(f"sizdan {summa} yechib olindi")

def send_money(account):
    account_number = int(input("account numberni kiriting ::: "))
    user_account = bank.find_account_by_account_number(account_number)
    summa = float(input(f"necha pul o'tkazmoqchisiz {user_account.owner_name}ga  :::: "))
    res = account.withdraw(summa)
    if res:
        user_account.add_balance(summa)
        print(f"Pulingiz {user_account.owner_name} ga ko'chirildi !")
    else:
        print("mablag' yetarli emas")


def make_task(account):
    while True:
        bank_menu()
        n = int(input("tanlang ::::: "))
        match n:
            case 1:
                print(f"Balansingiz {account.get_balance()} dollar")
            case 2:
                add_balance(account)
            case 3:
                withdraw_balance(account)
            case 4:
                send_money(account)
            case 0:
                break
            case _:
                print("Bunday menu mavjud emas !")



def hisob_ochish():
    name = input("Ismingizni kiriting :::: ")
    balance = float(input("Hisobni qanchaga tuldirmoqchisiz :::: "))
    pin_code = int(input("Pin kodni kiriting :::: "))
    account = BankAccount(
        n=len(bank.accounts) + 1,
        name=name,
        balance=balance,
        pin_code=pin_code
    )
    bank.add_account(account)
    print("account created successfully !!!")


def hisobga_kirish():
    pin_code = int(input("kirish uchun pin kodizni kriiting ... :::: "))
    account = bank.find_account_by_pincode(pin_code)
    if account:
        make_task(account)
    else:
        print("Bunday account topilmadi !")




def main():
    command = {
        1 : hisob_ochish,
        2 : hisobga_kirish,
        0 : print("Tizim yopildi!! Hayr. ")
    }   
    while True:
        menu()
        order_n = int(input("tanlang :::: "))
        res =  command.get(order_n,False)
        if not res:
            break
        res()
        
main()