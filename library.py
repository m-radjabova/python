# console  kutubxona 
# kitob qo'shish
# nomi, mavjudmi : False

# kitoblar ko'rish
# o'tkan kunlar kitobi hozirda mavjud
# qozoq askarlari kitobi hozirda mavjud emas

# kitobni uchirish
# tartib raqami bilan uchirish

# kitob debt qarzga berish
# 1 ---  o'tkan kunlar
# 2 --- qozoq askarlari

# kitobni qaytarish
# 1 ---  o'tkan kunlar
# 2 --- qozoq askarlari
# 2 --- qozoq daraxtlari
# 2 --- qozoq tarixi

# 1 o'tkan kunlar - 

# kitob qidirish 
# izlayotgan kitob nomini kiriting ...
# Qozoq



books = [{"id" : "1 ","name" : "o'tkan kunlar", "mavjudmi" : True}, 
{"id" : "2 ","name" : "qozoq askarlari","mavjudmi" : False}]

def main():
    while True:
        print("-------------------")
        print("1 --- kitob qo'shish 📚")
        print("2 --- kitoblar ko'rish 💫")
        print("3 --- kitobni uchirish 🗑️")
        print("4 --- kitob debt qarzga berish 📖")
        print("5 --- kitobni qaytarish 📖")
        print("6 --- kitob qidirish 🔎")
        print("-------------------")

        tanla = int(input("Tanlang: "))

        match tanla:
            case "1":
                add_book()
            case "2":
                show_books()
            case "3":
                delete_book()
            case "4":
                qarzga_berish()
            case "5":
                qaytarib_olish()
            case "6":
                search_book()
            case _:
                print("1-6 gacha son kiriting!!")


def add_book():
    name = input("📖 kitob nomini kiriting ---> ")
    books.append({
        "id" : len(books) + 1,
        "name" : name,
        "mavjudmi" : True
    })
    print("Yangi kitob qo'shildi!! ⭐️")

def show_books():
    for i, book in enumerate(books):
        print(f"{i + 1} --- {book['name']} {'mavjud' if book['mavjudmi'] else 'mavjud emas'}")

def delete_book():
    show_books()
    n = int(input("📖 qaysi kitobni o'chirmoqchisiz? "))
    index = n - 1
    books.pop(index)
    print(f"{books[n]["name"]} kitob o'chirildi!! ⭐️ ")


def qarzga_berish():
    show_books()
    n = int(input("📖 qaysi kitobni qarzga bermoqchisiz? "))
    index = n - 1
    books[index]["mavjudmi"] = False
    print(f"{books[n]["name"]} kitob qarzga berildi!! ⭐️ ")


def qaytarib_olish():
    show_books()
    n = int(input ("📖 qaysi kitobni qaytarib bermoqchisiz? "))
    index = n - 1
    books[index]["mavjudmi"] = True
    print(F"{books[n]["name"]} - kitob qaytarib topshirildi!! ⭐️ ")


def search_book():
    show_books()
    name = input("📖 Qaysi kitobni qidirmoqchisiz?: ").lower()
    found = False
    for i, book in enumerate(books):
        if book["name"].lower().startswith(name):
            print(f"{i + 1} --- {book['name']} {'mavjud' if book['mavjudmi'] else 'mavjud emas'}")
            found = True
    if not found:
        print("Bunday kitob mavjud emas!!")


main()