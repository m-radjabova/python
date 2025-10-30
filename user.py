import os

class User:
    def __init__(self, id: int, name: str, password: int, email: str, is_admin: bool):
        self.id = id
        self.name = name
        self.password = password
        self.email = email
        self.is_admin = is_admin


class Users:
    def __init__(self, filename="users.txt"):
        self.filename = filename
        self.users = self.load_users()

        if not any(u.is_admin for u in self.users):
            admin = User(1, "Admin", 1234, "admin@gmail.com", True)
            self.users.append(admin)
            self.save_users()

    def load_users(self):
        users = []
        if not os.path.exists(self.filename):
            return users

        with open(self.filename, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 5:
                    try:
                        id = int(parts[0])
                        name = parts[1]
                        password = int(parts[2])
                        email = parts[3]
                        is_admin = parts[4].lower() == "true"
                        users.append(User(id, name, password, email, is_admin))
                    except ValueError:
                        continue
        return users

    def save_users(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            for user in self.users:
                file.write(f"{user.id},{user.name},{user.password},{user.email},{user.is_admin}\n")

    def add_user(self):
        try:
            name = input("👤 Ismingizni kiriting: ")
            email = input("📧 Emailingizni kiriting: ")
            password = int(input("🔑 Parolni kiriting (faqat raqam): "))
            new_user = User(len(self.users) + 1, name, password, email, False)
            self.users.append(new_user)
            self.save_users()
            print(f"✅ {name} muvaffaqiyatli ro‘yxatdan o‘tdi!\n")
        except ValueError:
            print("⚠️ Parol faqat raqam bo‘lishi kerak!")
