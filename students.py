# 1 --- talaba qushish
# 2 --- talabalarni ko'rish
# 3 --- talaba uchirish
# 4 --- talaba yangilash

# 1 bosilganda
# foydalanuvchidan talabani ismi familiyasi va tug'ilgan yilini so'raymiz, emailini
# shu talabanni siz talabalar ruyhatga qushib qoyasiz
# qushish jarayonida agar bir xill emailli talaba mavjud bulsa , bunday emailli talaaba
# mavjud deyish


#  2 -  ko'rish
# 1 -- Hasan Rasulov 2000 yil email : hasan@gmail.com
# 2 -- Husan Rasulov 2000 yil email : husan@gmail.com

# 3 --- uchirish
# Qaysi talabani uchirmoqchisiz ?  talaba numberni kiriting ...
# 1 --- Hasan Rasulov
# 2 --- Husan Rasulov


# 4 --- update
# Qaysi talabani yangilamoqchisiz ?  talaba numberni kiriting ...
# 1 --- Hasan Rasulov
# 2 --- Husan Rasulov

# ismi , familiyasi , emailli
# muvvafiqayatli bajarildi



students = [{
    "name" : "Muslima",
    "last_name" : "Radjabova",
    "year": "2006",
    "email": "@muslima@gmail.com"
}]

def addStudent():
    name = input("Ismingizni kiriting : ")
    last_name = input("Familyangizni kiriting : ")
    email = input("Emailingizni kiriting : ")
    year = input("Tug'ilgan yilingizni kiriting : ")

    if(email in [student["email"] for student in students]):
        print("Bunday email mavjud!")
    else:
        students.append({
            "name" : name,
            "last_name" : last_name,
            "year": year,
            "email": email
        })
        print("Muvaffaqiyatli qushildi!!!")


def viewStudents():
       for student in range(len(students)):
            print(f"""{student + 1}. name: {students[student]["name"]}\nlast name: {students[student]["last_name"]}\nemail: {students[student]["email"]}\nyear: {students[student]["year"]} """)
            print(f"-------------------")



def deleteStudent():
    viewStudents()
    selected = int(input("qaysi talabani o'chirib tashlamoqchisiz? "))
    index = selected - 1
    students.pop(index)
    print(f"{selected} talaba muvaffaqiyatli o'chirildi")


def updateStudent():
    viewStudents()
    selected = int(input("qaysi talabani yangilamoqchisiz? "))
    index = selected - 1

    name = input("Ismingizni kiriting : ")
    last_name = input("Familyangizni kiriting : ")
    email = input("Emailingizni kiriting : ")
    year = input("Tug'ilgan yilingizni kiriting : ")

    students[index] = {
        "name" : name,
        "last_name" : last_name,
        "year": year,
        "email": email
    }
    print(f"{selected} talaba muvaffaqiyatli yangilandi")


while True: 
    print("-------------------")
    print("1 --- talaba qushish")
    print("2 --- talabalarni ko'rish")
    print("3 --- talaba uchirish")
    print("4 --- talaba yangilash")
    print("-------------------")

    tanla = input("Tanlang: ")

    match tanla:
        case "1":
            addStudent()
        case "2":
            viewStudents()
        case "3":
            deleteStudent()
        case "4":
            updateStudent()
