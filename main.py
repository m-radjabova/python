import math

# 1 misol 

# a = int(input("a sonini kirirting: "))
# p = 4 * a
# print(f"Perimetr: {p}")


# 2 misol
 
# a = int(input("a sonini kirirting: "))
# s = a ** 2
# print(f"kvadrati: {s}")


# 3 misol

# a = int(input("a sonini kirirting: "))
# b = int(input("b sonini kirirting: "))

# s = a * b
# p = 2 * (a + b)

# print(f"Perimetr: {p} va Uchburchakning yuzi: {s}")


# 4 misol

# d = int(input("d sonini kirirting: "))
# PI = 3.14

# l = PI * d

# print(f"diametri: {l}")


# 17 misol

# A = int(input("A nuqtani kirirting: "))
# B = int(input("B nuqtani kirirting: "))
# C = int(input("C nuqtani kirirting: "))

# AC = A + C
# BC = B + C

# d = AC + BC

# print(f"kesmalar uzunligi yigindisi:  {d}")


# 18 misol
# A = int(input("A nuqtani kirirting: "))
# B = int(input("B nuqtani kirirting: "))
# C = int(input("C nuqtani kirirting: "))


# d = A + C
# f = C + B 

# g = d + f

# print(f"kesmalar uzunligi yigindisi:  {g}")


#22 misol

# a = int(input("a sonini kirirting: "))
# b = int(input("b sonini kirirting: "))

# a, b = b, a

# print(f"a = {a} va b = {b}")


# 38 misol

# A = int(input("a koefisientini kirirting: "))
# B = int(input("b koefisientini kirirting: "))

# x= -B/A

# print(f"x = {x}")


# 39 misol

# A = int(input("a koefisientini kirirting: "))
# B = int(input("b koefisientini kirirting: "))
# C = int(input("c koefisientini kirirting: "))



# 40 misol 
# a1 = int(input("a1 sonini kirirting: "))
# b1 = int(input("b1 sonini kirirting: "))
# c1 = int(input("c1 sonini kirirting: "))
# a2 = int(input("a2 sonini kirirting: "))
# b2 = int(input("b2 sonini kirirting: "))
# c2 = int(input("c2 sonini kirirting: "))

# d = a1 * b2 - a2 * b1
# x = (c1 * b2 - b2 * c1) / d
# y = (a1 * c2 - c1 * a2) / d


# print(f"x = {x} va y = {y}")



# 1 misol

# L = int(input("Uzunlikni santimetrda kiriting: "))
# metr = L // 100
# print("To'liq metrlar soni:", metr)

# 2 misol

# M = int(input("Og'irlikni kilogramda kiriting: "))
# kg = M // 1000
# print("tonna soni:", kg)


# 3 misol

# b = int(input("baytlarni kiriting: "))
# kb = b // 1024
# print(f"Kilobaytlar soni: {kb}")

# 4 misol

# A = int(input("A ni kiriting: "))
# B = int(input("B ni kiriting: "))

# natija = A // B
# print(f"A kesmada B kesmani {natija} marta")

# 5 misol

# A = int(input("A ni kiriting: "))
# B = int(input("B ni kiriting: "))

# c = A // B
# d = A % B

# print(f"A kesmada B kesmani {c} marta mumkin")
# print(f"Joylashmagan qism: {d}")

# 6 misol

# x= int(input("sonni kiriting: "))

# last_digit = x % 10
# first_digit = x // 10

# print(f"Oxirgi raqam: {last_digit} va birinchi raqam: {first_digit}")

# 7 misol
# x= int(input("sonni kiriting: "))
# unlik = math.floor(x / 10)
# birlik = x % 10

# sum = unlik + birlik

# print(f"Unlik va birlik raqamlarini yigindisi: {sum}")

# 8 misol

# x= int(input("sonni kiriting: "))

# unlik = math.floor(x / 10)
# birlik = x % 10
# almashishi = (birlik * 10) + unlik

# print(f"Unlik va birlik raqamlarini almashtirish: {almashishi}")

# 9, 10, 11, 12, 13, 14, 15, 16 misol

# x= int(input("sonni kiriting: "))

# yuzlik = math.floor(x / 100)
# onlik = math.floor((x % 100) / 10)
# birlik = math.floor(x % 10)

# sum = yuzlik + onlik + birlik
# uzgarishi = (birlik * 100) + (onlik * 10) + yuzlik

# chapdan = (onlik * 100) + (birlik * 10) + yuzlik
# ondan = (birlik * 100) + (yuzlik * 10) + onlik

# almashtirish = (onlik * 100) + (yuzlik * 10) + birlik
# almashtirish2 = (yuzlik * 100) + (birlik * 10) + onlik

# print(f"Yuzlik raqamini yigindisi: {sum}")
# print(f"Uzgarish: {uzgarishi}")
# print(f"Chapdan: {chapdan}")
# print(f"Ondan: {ondan}")
# print(f"Almashtirish: {almashtirish}")
# print(f"Almashtirish2: {almashtirish2}")




#boolen34

# x = int(input("x sonni kiriting: "))
# y = int(input("y sonni kiriting: "))

# res= res = x % 2 != y % 2

# print(f"Natija: {res}")

#boolen35
# x1 = int(input("x1 sonni kiriting: "))
# y1 = int(input("y1 sonni kiriting: "))
# x2 = int(input("x2 sonni kiriting: "))
# y2 = int(input("y2 sonni kiriting: "))

# res = x2 % 2 == 0 and y2 % 2 == 0 or x2 % 2 == 1 and y2 % 2 == 1

# print(f"Natija: {res}")

# boolen36

# x1 = int(input("x1 sonni kiriting: "))
# y1 = int(input("y1 sonni kiriting: "))
# x2 = int(input("x2 sonni kiriting: "))
# y2 = int(input("y2 sonni kiriting: "))

# res =  x1 - x2 == 0 or y1 - y2 == 0

# print(f"Natija: {res}")

#boolen37
# x1 = int(input("x1 sonni kiriting: "))
# y1 = int(input("y1 sonni kiriting: "))
# x2 = int(input("x2 sonni kiriting: "))
# y2 = int(input("y2 sonni kiriting: "))

# res = abs(x2-x1) == 1 or abs(y2-y1) == 1 and (abs(x2-x1) == 1 and abs(y2-y1) == 1)

# print(f"Natija: {res}")


#boolen38
# x1 = int(input("x1 sonni kiriting: "))
# y1 = int(input("y1 sonni kiriting: "))
# x2 = int(input("x2 sonni kiriting: "))
# y2 = int(input("y2 sonni kiriting: "))


# res = abs(x1 - x2) == abs(y1 - y2) and (x1 != x2 or y1 != y2)

# print(f"Natija: {res}")


#boolen39

# x1 = int(input("x1 sonni kiriting: "))
# y1 = int(input("y1 sonni kiriting: "))
# x2 = int(input("x2 sonni kiriting: "))
# y2 = int(input("y2 sonni kiriting: "))

# res = (x1 == x2) or (y1 == y2) or (abs(x1 - x2) == abs(y1 - y2))

# print(f"Natija: {res}")

# boolen40
# x1 = 3
# x2 = 1
# y1 = 6
# y2 = 7

# res =  (abs(y2 - y1) == 2 and abs(x2 - x1) == 1) or (abs(y2 - y1) == 1 and abs(x2 - x1) == 2)
# print(res)



#integer24

# n = int(input("Sonni kiriting (1-365): "))

# kunlari = {
#     1: "dushanba",
#     2: "seshanba", 
#     3: "chorshanba",
#     4: "payshanba",
#     5: "juma",
#     6: "shanba",
#     0: "yakshanba"
# }

# m = n % 7
# kuni = kunlari.get(m, "mavjud emas")

# print(f"{n}-kun: {kuni}")


#integer25

# n = int(input("Sonni kiriting (1-365): "))

# m = (n + 3) % 7

# kunlari = {
#     1: "dushanba",
#     2: "seshanba", 
#     3: "chorshanba",
#     4: "payshanba",
#     5: "juma",
#     6: "shanba",
#     0: "yakshanba"
# }

# kuni = kunlari.get(m, "yakshanba")

# print(f"{n}-kun: {kuni}")


#integer26
# n = int(input("Sonni kiriting (1-365): "))

# m = (n + 1) % 7

# kunlari = {
#     1: "dushanba",
#     2: "seshanba", 
#     3: "chorshanba",
#     4: "payshanba",
#     5: "juma",
#     6: "shanba",
#     0: "yakshanba"
# }

# kuni = kunlari.get(m, "yakshanba")
# print(f"{n}-kun: {kuni}")

#integer27
# k = int(input("Sonni kiriting (1-365): "))

# n = (k - 1) % 7 + 1

# kunlari = {
#     1: "yakshanba",
#     2: "dushanba", 
#     3: "seshanba",
#     4: "chorshanba",
#     5: "payshanba",
#     6: "juma",
#     7: "shanba"
# }

# kuni = kunlari.get(n, "mavjud emas")
# print(f"{k}-kun: {kuni}")

#integer30

# y = int(input("Yilni kiriting: "))

# asr = y // 100 + 1

# print(f"{y} yilining asri: {asr}")



# while1

# A = int(input("A sonini kiriting: "))
# B = int(input("B sonini kiriting: "))

# while A >= B:
#         A = A - B

# print(A)

# while2

# A = int(input("A sonini kiriting: "))
# B = int(input("B sonini kiriting: "))
# count = 0 

# while A >= B:
#         A = A - B
#         count += 1

# print(f"oylashtirish mumkin bo‘lgan B kesmalar soni: {count}")

# while3
# N = int(input("N sonini kiriting: "))
# K = int(input("K sonini kiriting: "))

# butun_qism = 0

# while N >= K:
#     N = N - K     
#     butun_qism += 1 

#     qoldiq = N  
    
# print(f"butun qismi: {butun_qism}, qoldiq: {qoldiq}")


# while4
# n = 12
# x = 1

# while n > x:
#     x = x * 3

# if x == n:
#     print("3 ning darjasi")
# else:
#     print("3 ning darjasi emas")


# while5
# n = 12
# x = 1 
# count = 0

# while x < n:
#     x = x * 2   
#     count += 1

# if x == n:
#     print(f"{ count} 2 ning darjasi")
# else:
#     print("2 ning darjasi emas")


# while6
# i = 10
# a = 1

# while a > 1:
#     a *= i
#     i = i -2

# print(a)

# while24
# n = int(input("n sonini kiriting: "))
# f1 = 1
# f2 = 1

# while f2 < n:
#     temp = f1 + f2  
#     f1 = f2
#     f2 = temp

# print(f"fibonachi soni: {f1}")





#case 4 oy raqami berilgan shu oyda nechta kun borligini aniqlovchi programma tuzilsin

# n = int(input("Oy raqamini kiriting: "))

# match n:
#     case 1 | 3 | 5 | 7 | 8 | 10 | 12:
#         print("31 kun")
#     case 2 :
#         print("28 kun")
#     case 4 | 6 | 9 | 11 :
#         print ("30 kun")

class Solution:
    def romanToInt(self, s: str) -> int:
        nums = {
            "I" = 1,
            "V" = 5,
            "X" =  10,
            "L" = 50,
            "C" = 100,
            "D" = 500,
            "M" = 1000
        }


#case 5

# a = int(input("a sonini kiriting... "))
# b = int(input("b sonini kiriting... "))

# operator = int(input("1 - qoshish, 2 - ayirish, 3 - ko'paytirish, 4 - bo'lish: "))

# res = 0

# match operator: 
#     case 1:
#         res = a + b
#         print(f"natija: {res}")
#     case 2:
#         res = a - b
#         print(f"natija: {res}")
#     case 3:
#         res = a * b
#         print(f"natija: {res}")
#     case 4:
#         res = a / b
#         print(f"natija: {res}")


#case 6
# unit = int(input("Uzunlik birlikni kiriting (1 - desimetr, 2 - kilometr, 3 - metr, 4 - millimetr, 5 - santimetr):"))
# uzunlik = int(input("Kesma uzunligini kiriting: "))

# uzunlikmetrda = 0

# match unit: 
#     case 1:
#         uzunlikmetrda = uzunlik / 10
#         print(f"{uzunlik} desimetr {uzunlikmetrda} metr.")
#     case 2:
#         uzunlikmetrda = uzunlik * 1000
#         print(f"{uzunlik} kilometr {uzunlikmetrda} metr.")
#     case 3:
#         uzunlikmetrda = uzunlik
#         print(f"{uzunlik} metr {uzunlikmetrda} metr.")
#     case 4:
#         uzunlikmetrda = uzunlik / 1000
#         print(f"{uzunlik} millimetr {uzunlikmetrda} metr.")
#     case 5:
#         uzunlikmetrda = uzunlik / 100
#         print(f"{uzunlik} santimetr {uzunlikmetrda} metr.")


#case 7
# unit = int(input("Og'irlik birligini kiriting (1 - kilogramm, 2 - milligramm, 3 - gramm, 4 - tonna, 5 - sentner):"))
# ogirlik = int(input("Og'irlikni kiriting: "))

# ogirlikkgda = 0

# match unit: 
#     case 1:
#         ogirlikkgda = ogirlik
#         print(f"{ogirlik} kilogramm {ogirlikkgda} kilogramm.")
#     case 2:
#         ogirlikkgda = ogirlik / 1000
#         print(f"{ogirlik} milligramm {ogirlikkgda} kilogramm.")
#     case 3:
#         ogirlikkgda = ogirlik / 100
#         print(f"{ogirlik} gramm {ogirlikkgda} kilogramm.")
#     case 4:
#         ogirlikkgda = ogirlik * 1000
#         print(f"{ogirlik} tonna {ogirlikkgda} kilogramm.")
#     case 5:
#         ogirlikkgda = ogirlik * 100
#         print(f"{ogirlik} sentner {ogirlikkgda} kilogramm.")


#case 8

# D = int(input("Kunni kiriting:"))
# M = int(input("Oyni kiriting:"))

# match M:
#     case 1:
#         print(f"{D}.yanvar")
#     case 2:
#         print(f"{D}.fevral")
#     case 3:
#         print(f"{D}.mart")
#     case 4:
#         print(f"{D}.aprel")
#     case 5:
#         print(f"{D}.may")
#     case 6:
#         print(f"{D}.iyun")
#     case 7:
#         print(f"{D}.iyul")
#     case 8:
#         print(f"{D}.avgust")
#     case 9:
#         print(f"{D}.sentabr")
#     case 10:
#         print(f"{D}.oktabr")
#     case 11:
#         print(f"{D}.noyabr")
#     case 12:
#         print(f"{D}.dekabr")


#case 9
# yil = int(input("Yilni kiriting: "))
# oy = int(input("Oyni kiriting: "))
# kun = int(input("Kunni kiriting: "))

#case 16
# yosh = int(input("Yoshingizni kiriting (20–69 oralig'ida): "))

# onlik = yosh // 10
# birlik = yosh % 10

# match onlik:
#     case 2:
#         onlik_soz = "yigirma"
#     case 3:
#         onlik_soz = "o'ttiz"
#     case 4:
#         onlik_soz = "qirq"
#     case 5:
#         onlik_soz = "ellik"
#     case 6:
#         onlik_soz = "oltmish"
#     case _:
#         onlik_soz = ""

# match birlik:
#     case 0:
#         birlik_soz = ""
#     case 1:
#         birlik_soz = "bir"
#     case 2:
#         birlik_soz = "ikki"
#     case 3:
#         birlik_soz = "uch"
#     case 4:
#         birlik_soz = "to'rt"
#     case 5:
#         birlik_soz = "besh"
#     case 6:
#         birlik_soz = "olti"
#     case 7:
#         birlik_soz = "yetti"
#     case 8:
#         birlik_soz = "sakkiz"
#     case 9:
#         birlik_soz = "to'qqiz"
#     case _:
#         birlik_soz = ""

# if 20 <= yosh <= 69:
#     if birlik == 0:
#         print(f"{onlik_soz} yosh")
#     else:
#         print(f"{onlik_soz} {birlik_soz} yosh")
# else:
#     print("Faqat 20 dan 69 gacha bo'lgan son kiriting!")


#case 17
# son = int(input("masala sonini kiriting (10 dan 40gacha): "))

# onlik = son // 10
# birlik = son % 10

# match onlik:
#     case 1:
#         onlik_soz = "o'n"
#     case 2:
#         onlik_soz = "yigirma"
#     case 3:
#         onlik_soz = "o'ttiz"
#     case 4:
#         onlik_soz = "qirq"
#     case _:
#         onlik_soz = ""


# match birlik:
#     case 0:
#         birlik_soz = ""
#     case 1:
#         birlik_soz = "bir"
#     case 2:
#         birlik_soz = "ikki"
#     case 3:
#         birlik_soz = "uch"
#     case 4:
#         birlik_soz = "to'rt"
#     case 5:
#         birlik_soz = "besh"
#     case 6:
#         birlik_soz = "olti"
#     case 7:
#         birlik_soz = "yetti"
#     case 8:
#         birlik_soz = "sakkiz"
#     case 9:
#         birlik_soz = "to'qqiz"
#     case _:
#         birlik_soz = ""

# if 10 <= son <= 40:
#     if birlik == 0:
#         print(f"{onlik_soz}ta masala")
#     else:
#         print(f"{onlik_soz} {birlik_soz}ta masala")
# else:
#     print("Iltimos, 10 dan 40 gacha bo'lgan son kiriting!")
