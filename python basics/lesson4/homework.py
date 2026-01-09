# cars = ['toyoto','mazda','gm','kia']
# for car in cars:
#     if car.lower() == 'gm':
#         print(car.upper())
#     else:
#         print(car.title())

# cars = ['toyoto','mazda','gm','kia']
# for car in cars:
#     if car.lower() != 'gm':
#         print(car.title())
#     else:
#         print(car.upper())

# ism = input('Login ismingizni kiriting: ')
# if ism.lower() == 'admin':
#     print("Xush kelibsiz, Admin!")
# else:
#     print("Xush kelibsiz", ism.title())

# num1 = float(input("1-chi sonni kiriting: "))
# num2 = float(input("2-chi sonni kiriting: "))
# if num1 == num2:
#     print("Bu sonlar teng!", num1, "=", num2)

# son = float(input("istalgan sonni kiriting: "))
# if son>0:
#     print(son, "Musbat son")
# else:
#     print(son, "Manfiy son")

# son = float(input("Son kiriting: "))
# if son>0:
#     print(son**0.5)
# else:
#     print("Musbat son kiriting!")

# son = float(input("Son kiriting: "))
# if son%2 == 0:
#     print("Juft son")
# else: 
#     print("Toq son")

# kun = input("Bugun kun nima: ")
# if kun.lower() == 'shanba' or kun.lower() == 'yakshanba':
#     print("Bugun dam olish kuni!")
# else : print("Bugun ish kuni!")

# narx = 15000
# choy = False
# salat = True
# if choy and salat:
#     narx += 10000
# elif choy or salat:
#     narx += 5000
# print(narx)

# narx = 15000
# choy = True
# salat = True
# non = False

# if choy:
#     print("Choy olindi.")
#     narx += 5000
# if salat:
#     print("Salat olindi.")
#     narx += 6000
# if non:
#     print("Non olindi.")
#     narx += 7000
# print(f"Jami {narx} so'm bo'ldi.")

# menu = ['osh','manti','baliq']
# ovqat = input("Nima ovqat yeysiz: ")
# if ovqat.lower() in menu:
#     print("Buyurtma qabul qilindi!")
# else: print("Bizda bunday taom yo'q!")

# a = 6
# print(a != 5)

# menu = ['osh','manti','baliq']
# print('kabob' in menu)

# menu = ['osh','manti','baliq']
# buyurtmalar = ['osh','manti']

# for taom in buyurtmalar:
#     if taom in menu:
#         print(f"Bizda {taom} bor!")
#     else: print(f"Bizda {taom} yoq!!!")

# list = [1,2,3]
# print(len(list)>0)

# list = []
# print(len(list)>0)

# list = [1,2,3]
# if list:
#     print("Ro'yxat bo'sh emas!")

"""Amaliyot"""

# son = int(input("Juft son kiriting: "))
# if son % 2 == 0:
#     print("Raxmat")
# else: print("Bu juft son emas.")

# print(20%2)

# yosh = int(input("Yoshingizni kiriting: "))
# if yosh<4 or yosh>60:
#     narx = 0
# elif yosh<18: narx = 10000
# else: narx = 20000
# print(f"Chipta {narx} so'm")

# son1 = float(input("Birinchi sonni kiriting: "))
# son2 = float(input("Ikkinchi sonni kiriting: "))
# if son1 > son2:
#     print(f"{son1} > {son2}")
# elif son1 == son2: print(f"{son1} = {son2}")
# else: print(f"{son1} < {son2}")

# mahsulot = ['olma','kartoshka','kitob','daftar','ruchka','qalam']
# savat = []
# print("3 ta mahsulot kiriting: ")
# for i in range(3):
#     savat.append(input(f"{i+1} - mahsulotni kiriting: "))
# for a in savat:
#     if a.lower() in mahsulot:
#         print(f"Bizda {a} bor!")
#     else: print(f"Bizda {a} yoq!")

# foydalanuvchilar = ["Ali","vali","Doni","Zafar","rano"]
# login = input("Login tanlang: ")
# if login in foydalanuvchilar:
#     print("Bu olingan")
# else: print("Xush kelibsiz")

# son = int(input("Butun son kiriting: "))
# for a in range(2,11):
#     if not son%a:
#         print(a)

# sonlar = []
# for i in range(3):
#     sonlar.append(float(input(f"{i+1}-sonni kiriting: ")))
# print("Eng katta son:", max(sonlar))
# print("Eng kichik son:", min(sonlar))

# son1 = float(input("1-sonni kiriting: "))
# son2 = float(input("2-sonni kiriting: "))
# son3 = float(input("3-sonni kiriting: "))
# son4 = float(input("4-sonni kiriting: "))
# if son1 >= son2 and son3>=son4:
#     if son1>=son3:
#         print(son1)
#     else: print(son3)
# else:
#     if son2>=son4:
#         print(son2)
#     else:print(son4)

# ismlar = ['alibek','vali','Asilbek','doni']
# for ism in ismlar:
#     if ism[-3:].lower() == 'bek':
#         print(ism)