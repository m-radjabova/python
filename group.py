# 1 --- Guruh qo'shish
# 2 --- Guruh o'chirish
# 3 --- Guruhga Student qo'shish
# 4 --- Guruhga o'qituvchi biriktirish

# 1 bosilganda 
# guruh nomini kiriting 
#  1kt-23
# guruh yaratildi

#  2 bosilganda
# guruhlar ruyhati ---- statusi True
#  1 --- 1kt-23
#  2 --- 2kt-23

#  1 tanlangandan sung , guruh uchirildi statusini False qilasiz



# 3 bosilganda --- guruhga student qushish
# guruhlar ruyhati ---- statusi True
#  1 --- 1kt-23
#  2 --- 2kt-23

# 1 - tanlangandan so'ng
# student nomi, email
#  student muvafiqatli qushildi


class Student:
    def __init__(self, id:int, name:str, age:int, phone:str, email:str):
        self.id = id
        self.name = name
        self.age = age
        self.phone_number = phone
        self.email = email


class Teacher:
    def __init__(self, id:int, name:str, email:str):
        self.id = id
        self.name = name
        self.email = email


class Group:
    def __init__(self, id, name: str):
        self.id = id
        self.name = name
        self.students: list[Student] = []
        self.status = True
        self.teacher: Teacher = None

    def add_student(self, student: Student):
        self.students.append(student)

    def close_group(self):
        self.status = False

    def show_students(self):
        print(f"📋 {self.name} guruhi talabalari:")
        for index, student in enumerate(self.students):
            print(f"   👤 {index + 1}. {student.name} — 📧 {student.email}")
    
    def delete_student(self, id):
        self.students = [student for student in self.students if student.id != id]

    def assign_teacher(self, teacher: Teacher):
        self.teacher = teacher


groups: list[Group] = []


def main():
    while True:
        print("\n==============================")
        print("1️⃣  — Guruh qo'shish")
        print("2️⃣  — Guruhni yopish")
        print("3️⃣  — Guruhga student qo'shish")
        print("4️⃣ — Guruhdan student o'chirish")
        print("5 — Guruhga o'qituvchi biriktirish")
        print("6 — Studentlar ro'yxati")
        print("0️⃣  — Chiqish")
        print("==============================")
        tanla = int(input("Tanlang 👉 "))

        match tanla:
            case 1:
                add_group()
            case 2:
                delete_group()
            case 3:
                group_add_student()
            case 4:
                delete_group_student()
            case 5:
                group_assign_teacher()
            case 6 :
                show_students()
            case 0:
                print("👋 Dastur yakunlandi. Xayr!")
                break
            case _:
                print("⚠️  Iltimos, 0 dan 4 gacha bo'lgan raqamni kiriting!")

def add_group():
    name = input("📘 Guruh nomini kiriting: ")
    group = Group(len(groups) + 1, name)
    groups.append(group)
    print(f"✅ '{group.name}' guruhi muvaffaqiyatli qo'shildi!")


def show_students():
    show_groups()
    n = int(input("Qaysi guruhni studentlarini ko'rmoqchisiz?: "))
    group = groups[n - 1]
    group.show_students()


def show_groups():
    print("\n📋 Guruhlar ro'yxati:")
    for index, group in enumerate(groups): 
        if group.status == True : 
            print(f"{index + 1}. 🏫 guruh nomi: {group.name}")


def delete_group():
    show_groups()
    n = int(input("🗑 Qaysi guruhni o'chirmoqchisiz (raqamini kiriting): "))
    group = groups[n - 1]
    group.close_group()
    print(f"❎ '{group.name}' guruhi yopildi!")


def group_add_student():
    show_groups()
    n = int(input("👥 Qaysi guruhga student qo'shmoqchisiz: "))
    group = groups[n - 1]
    name = input("🧑‍🎓 Student nomi: ")
    email = input("📧 Student emaili: ")
    phone = input("📞 Student telefon raqami: ")
    age = int(input("🎂 Student yoshi: "))
    group.add_student(Student(len(group.students) + 1, name, age, phone, email))
    print(f"✅ {name} - '{group.name}' guruhiga qo'shildi!")


def group_assign_teacher():
    show_groups()
    n = int(input("👨‍🏫 Qaysi guruhga o'qituvchi biriktirmoqchisiz: "))
    group = groups[n - 1]
    name = input("👨‍🏫 O'qituvchi ismi: ")
    email = input("📧 O'qituvchi emaili: ")
    teacher = Teacher(group.id, name, email)
    group.assign_teacher(teacher)
    print(f"✅ O'qituvchi {name} - '{group.name}' guruhiga biriktirildi!")

def delete_group_student():
    show_groups()
    n = int(input("qaysi guruhdan student o'chirmoqchisiz: "))
    group = groups[n - 1]
    group.show_students()
    index = int(input("Studentni tanlang: "))
    student = group.students[index- 1]
    group.delete_student(student.id)
    print("Student o'chirildi!!")

main()