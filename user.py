class User:
    def __init__(self, id: int, name: str, password: int, email: str, is_admin:bool):
        self.id = id
        self.name = name
        self.password = password
        self.email = email
        self.is_admin = is_admin


class Users:
    def __init__(self):
        self.users = []
        admin = User(1, "Admin", 1234, "admin@gmail.com", True)
        self.users.append(admin)

    def add_user(self):
        name = input("👤 Ismingizni kiriting: ")
        email = input("📧 Emailingizni kiriting: ")
        password = int(input("🔑 Parolni kiriting: "))
        new_user = User(len(self.users) + 1, name, password, email, False)
        self.users.append(new_user)
        print(f"✅ {name} foydalanuvchi muvaffaqiyatli ro‘yxatdan o‘tdi!\n")
