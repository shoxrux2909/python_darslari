# son = 50
# if son>=0:
#     print("Musbat son")
# else:
#     print("Manfiy son")

# son = input("Istalgan son kitirting")
# print(f"{son} ning kvadrati {son**2} ga teng.")

# prit("hulla")

# son = int(input('Istalgan sonni k'))
# if son>0:
#     print("Musbat son")
# else: 
#     print("Manfiy son")

# mevalar = ['olma','nok','uzum']
# print(mevalar[9])
"""Amaliyot"""

# son = float(input("Juft son kiriting: "))
# if son%2 != 0:
#     print("Rahmat!")
# else:
#     print("Bu son juft emas.")

# yosh = int(input("Yoshingizni kiriting?"))

# if yosh<4 or yosh>=60:
#     narx = 0 
# elif yosh<18:
#     narx = 10000
# else:
#     narx = 20000
#     print(f"Chipta {narx} so'm")

# x = float(input("Birinchi sonni kiriting: "))
# y = float(input("Ikkinchi sonni kiriting: "))
# if x == y:
#     print(f"{x}={y}")
# elif x<y:
#     print(f"{x}<{y}")
# else:
#     print(f"{x}>{y}")

# mahsulotlar = ['un',"yo'g",'sovun','tuxum','piyoz',
#                'kartoshka','olma','bana','qovun']
# savat = []
# for n in range(5):
#     savat.append(input(f"{n+1}-mahsulotni qo'shing: "))

# if savat:
#     for mahsulot in savat:
#         if mahsulot in mahsulotlar:
#             print(f"Do'konimizda {mahsulot} bor")
#         else:
#             print(f"Do'konimizda {mahsulot} yo'q")
# else:print("Savatingiz bo'sh")

# users = ['alisher1983','aziza','yasina','umar']

# login = input("Yangi login tanlang: ")
# if login in users:
#     print('Login band, yangi login tanlang!')
# else:
#     print("Xush kelibsiz!")

# yosh = input("Yoshingizni kiriting: ")
# try:
#     yosh = int(yosh)
# except ValueError:
#     print("Butun son kiritmadingiz.")
# else: print(f"{2025-yosh} yilda tug'ilgansiz.")

# x,y = 6,10
# try:
#     print(y/(x-5))
# except ZeroDivisionError:
#     print("o ga bo'lib bo'lmaydi.")

# mevalar = ['olma','nok','anor']
# try:
#     print(mevalar[4])
# except IndexError:
#     print(f"Ro'yxatda {len(mevalar)} ta meva bor.")

# user = {
#     "username":"shoxrux",
#     "status":"student",
#     "email":"sh.abdullayev2003",
#     "phone":"943372909"
# }
# key = "phone"
# try:
#     print(f"Foydalanuvchi: {user[key]}")
# except KeyError:
#     print('Bunday kalit mavjud eams!')

# fayl = "data.txt"
# try:
#     f = open(fayl)
# except FileNotFoundError:
#     print(f"{fayl} fayli mavjud emas.")

# n = input("Butun son kiriting: ")
# try:
#     n = int(n)
#     x = 20/n
# except ValueError:
#     print("Butun son kiritmadingiz.")
# except ZeroDivisionError:
#     print("0 ga bo'lib bo'lmaydi.")
# else:
#     print(f"x={x}")

# if yosh<20:
#     pass
# else: pass

# while True:
#     yosh = input("Yoshingizni kiriting: ")
#     if yosh.isdigit():
#         yosh = int(yosh)
#         break
# print(f"Siz {2021-yosh} yilda tug'ilgansiz.")
"""Amaliyot"""

# while True:
#     try:
#         x = int( input( "son kiriting: ") )
#         y = int( input( "yana son kiriting: " ) )
#     except ValueError:
#         print("Siz butun son kiritmadingiz!")
#     else:
#         print( x, '/' , y, '=', x/y)

# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalomu alaykum")

# def salom_ber(ism):
#     """Foydalanuvchiga salom beruvchi funksiya"""
#     print(f"Assalomu alaykum, hurmatli {ism.title()}!")

# print(salom_ber.__doc__)

# def tuliq_ism(ism,familiya):
#     """ism va familiyani jamlab chiqaruvchi funksiya"""
#     print(f"Foydalanuvchi ismi: {ism.title()} \n"
#           f"Foydalanuvhi familiyasi: {familiya.title()}")

# tuliq_ism("akbar","holiqov")

# def yosh_hisobla(ism, tyil):
#     """Foydalanuvchi yoshini hisoblaydigan funksiya"""
#     print(f"{ism.title()} ning yoshi {2025-tyil} da.")

# yosh_hisobla(ism="anvar",tyil=2000)

# def yosh_hisobla(tyil,joriy_yil=2025):
#     print(f"Siz {joriy_yil-tyil} yoshdasiz.")

# yosh_hisobla(2020,2040)
"""Amaliyot"""
# def tyil_hiobla(ism,yosh):
#     """tug'ilgan yilini hisoblaydigan funksiya"""
#     print(f"Foydalanuvchi ismi: {ism.title()}\n"
#           f"Foydalanuvchi tug'ilgan yili: {2025-yosh}")

# tyil_hiobla("anvar",26)

# def kub_kvadrat(number):
#     """Sonni kubi va kvadratini chiqarish"""
#     print(f"Sonning kvadrati: {number**2}\n"
#           f"Sonning kubi: {number**3}")

# kub_kvadrat(4)

# def just_yoki_toq(number):
#     """Juft yoki toqligini chiqarish"""
#     if number % 2:
#         print(f"{number} toq son")
#     else: print(f"{number} juft son")

# just_yoki_toq(4)

# def katta_son(number1,number2):
#     """Sonlarni taqqoslash"""
#     if number1>number2:
#         print(f"{number1}>{number2}")
#     elif number1 == number2:
#         print(f"{number1}={number2}")
#     else:
#         print(f"{number1}<{number2}")

# katta_son(41,58)

# def x_ning_n_darajasi(x,n):
#     """x ning n darajasini chiqarish"""
#     print(f"{x} ning {n} darajasi: {x**n}")

# x_ning_n_darajasi(4,3)

# def x_ning_n_darajasi(x,n=2):
#     """x ning n darajasini chiqarish"""
#     print(f"{x} ning {n} darajasi: {x**n}")

# x_ning_n_darajasi(4)

def bulinish(number):
    """Sonni 2 dan 10 gacha bo'linishini tekshirish"""
    for n in range(2,11):
        if number%n ==0:
            print(f"{number} soni {n} ga bo'linadi. ✅")
        else:
            print(f"{number} soni {n} ga bo'linmaydi.")

bulinish(7)
