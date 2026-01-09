"""Amaliyot
146-156-bet
"""

# while True:
#     try:
#         x = int(input("son k: "))
#         y = int(input("son k: "))
#         print(x/y)
#     except ValueError:
#         print("int son kiriting.")
#     except ZeroDivisionError:
#         print("Nolga bo'lib bo'lmaydi.")
#     except Exception as e:
#         print(f"caught an error: {e}")

# def tugilgan_yil(ism,yosh):
#     t_yil = 2025 - yosh
#     return f"{ism.title()}, {t_yil}"
# print(tugilgan_yil(ism="Akbar",yosh=26))

# def kvadrat_kub(son):
#     return f"Sonning kvadrat: {son**2} \nSonning kubi: {son**3}"
# print(kvadrat_kub(son=5))

# def juft_toq(son):
#     if son%2:
#         return "Toq"
#     return "Juft"
# print(juft_toq(son=5))

# def katta_son(num1,num2):
#     if num1 > num2:
#         return num1
#     elif num1 == num2:
#         return "Sonlar teng"
#     return num2
# print(katta_son(num1=44,num2=56))
# print(katta_son(num1=7,num2=7))

# def x_ning_n_darajasi(x,n=2):
#     return x**n
# print(x_ning_n_darajasi(x=2))
# print(x_ning_n_darajasi(x=7,n=3))


# def bulinish(x):
#     for n in range(2,11):
#         if x%n == 0:
#             print(f"{x} soni {n} ga bo'linadi. ✅")
#         else:
#             print(f"{x} soni {n} ga bo'linmaydi.")

# bulinish(45)

# def toliq_ism_yasa(ism,familiya):
#     """To'liq ism qaytaruvchi funksiya"""
#     toliq_ism = f"{ism} {familiya}"
#     return toliq_ism

# print(toliq_ism_yasa("Akbar","Sobirov"))
# print(toliq_ism_yasa(ism="Anvar",familiya="Rahmonov"))

# def toliq_ism_yasa(ism,familiya,otasini_ismi=""):
#     if otasini_ismi:
#         toliq_ism = f"{ism} {familiya} {otasini_ismi}"
#     else:
#         toliq_ism = f"{ism} {familiya}"
#     return toliq_ism
# print(toliq_ism_yasa(ism="Anvar",familiya="Rahmonov",otasini_ismi="Botir o'g'li"))

# def avto_info(make,model,rangi,korobka,yili,narxi=None):
#     avto = {
#         "kompaniya":make,
#         "model":model,
#         "rang":rangi,
#         "korobka":korobka,
#         "yil":yili,
#         "narxi":narxi
#     }
#     return avto

# avto1 = avto_info("GM","Malibu","Qora","Avtomat","2018")
# avto2 = avto_info("GM","Gentra","Oq","Mexanika",2016,15000)
# avtolar = [avto1,avto2]
# print("Online bozordagi mavjud avtomashinalar: ")
# for avto in avtolar:
#     if avto['narxi']:
#         narx = avto["narxi"]
#     else:
#         narx = "Noma'lum"
#     print(f"{avto['rang']} {avto["model"]}. Narxi: {narx}")

# def oraliq(min,max,qadam=1):
#     sonlar = []
#     while min<max:
#         sonlar.append(min)
#         min += qadam
#     return sonlar

# print(oraliq(1,11))
# print(oraliq(10,21))
# print(oraliq(1,23,3))

# def avto_info(make,model,rangi,korobka,yili,narxi=None):
#     avto = {
#         "kompaniya":make,
#         "model":model,
#         "rang":rangi,
#         "korobka":korobka,
#         "yil":yili,
#         "narxi":narxi
#     }
#     return avto

# print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
# avtolar = []
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting.")
#     kompaniya = input("Ishlab chiqaruvchi: ")
#     model = input("Modeli: ")
#     rangi = input("Rangi: ")
#     korobka = input("Korobka: ")
#     yili = input("Ishlab chiqarilgan yili: ")
#     narxi = input("Narxi: ")
#     avtolar.append(avto_info(kompaniya,model,kompaniya,\
#                              korobka,yili,narxi))
#     javob = input("Yana avto qo'shasizmi ? (yes\no): ")
#     if javob == "no":
#         break

# print(avtolar)
