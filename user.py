class User:
    def __init__(self, id: int, name: str, password: int, email: str):
        self.id = id
        self.name = name
        self.password = password
        self.email = email


class Users:
    def __init__(self):
        self.users = []

    def add_user(self):
        name = input("👤 Ismingizni kiriting: ")
        email = input("📧 Emailingizni kiriting: ")
        password = int(input("🔑 Parolni kiriting: "))
        user = User(len(self.users) + 1, name, password, email)
        self.users.append(user)
        print(f"✅ {name} foydalanuvchi muvaffaqiyatli ro‘yxatdan o‘tdi!\n")
