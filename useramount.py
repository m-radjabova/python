# user qushish
# pul o'tkazmalari

# account = 84000

#  1 --- qarz berish
#  2 ---  qarz olish
#  user 1  amount  76000
#  user 2  amunt  60000

# user talangandan so'ng
# bizanni pulimizdan unga utkazadi
# qarz miqdorini kiriting : 6000
# unni pulidan bizaga utkazadi

class BankShot:
    def __init__(self, amount):
        self.account = amount

me = BankShot(150000)

class User:
    def __init__(self, name, balance, user_id):
        self.id = user_id
        self.name = name
        self.balance = balance



users: list[User] = []


def main():
    while True:
        print(f"my balance is {me.account}")
        print("1 -- User qo'shish")
        print("2 -- Qarz berish")
        print("3 -- Qarz olish")
        print("0 -- Chiqish")
        n = int(input("Tanlang: "))

        match n:
            case 1:
                add_user()
            case 2:
                debt_amount()
            case 3:
                borrow_amount()
            case 0:
                print("Dastur yakunlandi.")
            case _:
                print("Noto‘g‘ri tanlandi.")

def add_user():
    name = input("Ismingizni kiriting: ")
    balance = int(input("Mablag'ingizni kiriting: "))
    user = User(name, balance, len(users) + 1)
    users.append(user)
    print(f"{user.name} qo'shildi! Balans: {user.balance}")


def show_users():
    for i,user in enumerate(users):
        print(f"{i+1}. -- name: {user.name}, balance: {user.balance}")

def debt_amount():
    show_users()
    n = int(input("qaysi userga qarz bermoqchisiz: "))
    user = users[n-1]
    debt = int(input("qancha qarz bermoqchisiz? (Kiriting)...."))
    if debt <= me.account:
        me.account -= debt
        user.balance += debt
        print(f"{debt} so‘m {user.name}ga berildi.")
        print(f"{user.name} yangi balansi: {user.balance}")
        print(f"Mening balansim: {me.account}")
    else:
        print("Mablag' yetarli emas")

def borrow_amount():
    show_users()
    n = int(input("qaysi userdan qarz olmoqchisiz: "))
    user = users[n-1]
    debt = int(input("qancha qarz olmoqchisiz? (Kiriting)...."))
    if debt <= user.balance:
        me.account += debt
        user.balance -= debt
        print(f"{debt} so‘m {user.name}dan olindi.")
        print(f"{user.name} yangi balansi: {user.balance}")
        print(f"Mening balansim: {me.account}")
    else:
        print("Mablag' yetarli emas")

main()