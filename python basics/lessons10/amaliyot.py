"""Amaliyot

161 - bet """

# def foydalanuvchi(ism,familiya,tyil,tjoy,e_manzil="",tel_raqam=None):
#     user_dict = {
#         "ism":ism,
#         'familiya':familiya,
#         "tyil":tyil,
#         "tjoy":tjoy,
#         'e_manzil':e_manzil,
#         'tel':tel_raqam,
#         'yosh': 2025-tyil
#     }
#     return user_dict

# print("Foydalanuvchi haqida ma'lumotlarni kiriting.")
# users = []
# while True:
#     ism = input("Isimi: ")
#     familiya = input("Familiyasi: ")
#     tyil = int(input("Tug'ilgan yili: "))
#     tjoy = input("Tug'ilgan joyi: ")
#     e_manzil = input("Elektron manzili: ")
#     tel_raqam = input("Telefon raqami: ")
#     users.append(foydalanuvchi(ism,familiya,tyil,tjoy,e_manzil,tel_raqam))
#     javob = input("Yana user qo'shasizmi? (yes/no): ")
#     if javob == 'no':
#         break

# print("Foydalanuvchilar:")
# for user in users:
#     print(f"{user['ism'].title()} {user['familiya'].title()}, "
#           f"{user['yosh']} yoshda {user['tel']} - telefon raqami")

# def engkatta(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     else :
#         return c
    
# print("Uchta son kiritng:")
# a = float(input("Birinchi sonni kiriting: "))
# b = float(input("Ikkinchi sonni kiriting: "))
# c = float(input("Uchinchi sonni kiriting: "))
# print(engkatta(a,b,c))

# def kattasi(x,y,z):
#     max = x
#     if y >= max:
#         return y
#     if z >= max:
#         return z
#     return max

# print(kattasi(7,5,98))

# def aylana(r):
#     PI = 3.1415926535
#     d = 2*r
#     p = round(d*PI,2)
#     s = round(PI*(r**2),2)
#     return f"Diametri: {d}, Perimetri: {p}, Yuzi: {s}"

# print(aylana(3))

# def aylana_info(radius, pi=3.1415926535):
#     aylana = {
#         'radiusi':radius,
#         'diametri': 2*radius,
#         'perimetri': 2*radius*pi,
#         'yuzi': pi*radius**2
#     }
#     return aylana

# print(aylana_info(radius=8))

# def tubsonlar(min,max):
#     sonlar = []
#     for x in range(min,max+1):
#         tub = True
#         if x <= 0:
#             continue
#         elif x == 1:
#             tub = False
#         elif x == 2:
#             tub = True
#         else:
#             for n in range(2,x):
#                 if x % n == 0:
#                     tub = False
#         if tub:
#             sonlar.append(x)
#     return sonlar
# print(tubsonlar(-22,20))

# def fibonachi(n):
#     sonlar = []
#     a=b=1
#     for i in range(n):
#         sonlar.append(a)
#         a,b = b,a+b
#     return sonlar

# print(fibonachi(14))
# 0 = 1
# 1 = 1
# 2 = 2 
# 3 = 3
# 4 = 5
# 5 = 8
# def fibonachi(n):
#     sonlar = []
#     for x in range(n):
#         if x==0 or x==1:
#             sonlar.append(1)
#         else:
#             sonlar.append(sonlar[x-1]+sonlar[x-2])
#     return sonlar

# print(fibonachi(14))

# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"{ism.title()} ning bahosini kiriting: ")
#         baholar[ism]=baho

#     return baholar

# talabalar = ['ali','vali','sobir']
# baholar = bahola(talabalar[:])
# print(baholar)
# print(talabalar)

# def katta_birinchi_harf(list_):
#     dict_ = {}
#     for i in range(len(list_)):
#         dict_[i] = list_[i].title()
#     return dict_

# print(katta_birinchi_harf(talabalar))
# print(talabalar)

"""*args,**kwargs"""

# def summa(*sonlar):
#     yigindi = 0
#     for son in sonlar:
#         yigindi += son
#     return yigindi

# print(summa(1,2,3,4,5,6,7,8,9,10))

# def summa(*sonlar):
#     return sum(sonlar)

# print(summa(1,5,6,7))

# def avto_info(kompaniya,model,**malumotlar):
#     malumotlar["kompaniya"] = kompaniya
#     malumotlar["model"] = model
#     return malumotlar

# avto1 = avto_info("GM","lasetti",rang="qora",yil=2018)
# print(avto1)

"""Amaliyot"""

# def kupaytma(*sonlar):
#     kupaytmalar = 1
#     for son in sonlar:
#         kupaytmalar *= son
#     return kupaytmalar

# print(kupaytma(2,5,6,6))

# def talaba_info(ism,familiya,**talaba):
#     talaba["ismi"] = ism
#     talaba["familiyasi"] = familiya
#     return talaba

# talaba1 = talaba_info("Anvar","Rahmonov", guruh="212-20", tel=2151515)
# print(talaba1)

# import avto_info_mod
# avto1 = avto_info_mod.avto_info("GM","Malibu","Qora",'avtomat', 2020, 40000)
# avto_info_mod.info_print(avto1)

# from avto_info_mod import avto_info, info_print
# avto1 = avto_info("Gm","Malibu","Qora","avtomat",2020,40000)
# info_print(avto1)

# from avto_info_mod import avto_info as ainfo
# from avto_info_mod import info_print as iprint
# avto1 = ainfo("gm","malibu","Qora",'avtomat',2020,40500)
# iprint(avto1)

# from avto_info_mod import *
# avto1 = avto_info("gm",'malibu',"oq","korobka",2020,50000)
# info_print(avto1)

# import math
# x=400
# print(math.sqrt(36))
# print(pow(5,2,))

# from math import pi
# print(pi)

# import math
# print(math.pi)

# import math
# print(math.log2(8))
# print(math.log10(100))

# import random as r
# print(r.randint(2,10))
# son = r.randint(0,100)
# print(son)

# ismlar = ['olim','anvar','ali','vali']
# ism = r.choice(ismlar)
# print(ism)

# x = list(range(0,51,5))
# print(x)
# print(r.choice(x))

# x = list(range(11))
# print(x)
# r.shuffle(x)
# print(x)

# from random import sample as sp
# x = list(range(0,100))
# y = sp(x,10)
# print(y)

# import math 
# uzunlik = lambda pi,r : 2*pi*r
# print(uzunlik(math.pi,10))

# import math
# product = lambda x,y : x ** y
# print(product(2,3))

# from math import sqrt
# sonlar = list(range(11))
# ildizlar = list(map(sqrt,sonlar))
# print(ildizlar)

# def kvadratlar(*sonlar):
#     kvadratlar_list = []
#     for son in sonlar:
#         kvadratlar_list.append(son**2)
#     return kvadratlar_list

# print(kvadratlar(2,3,4,5,6,8))

# def ruyhat(**malumot):
#     return malumot
# print(ruyhat(ism='anvar',familiya='rahmonov'))

# sonlar = list(range(11))
# def daraja2(x):
#     return x*x

# print(list(map(daraja2,sonlar)))

# ismlar = ['ali','vali']
# def katta_harf(x):
#     return x.title()

# print(list(map(katta_harf,ismlar)))

# kvadratlar = list(map(lambda x: x*x,sonlar))
# print(kvadratlar)

# a = [1,2,3]
# b = [4,5,6]
# a_plus_b = list(map(lambda x,y : x+y,a,b))
# print(a_plus_b)

# ismlar = ['ali','vali','doni']
# familiyalar = ['aliyev','valiyev','doniyev']
# ism_familiya = list(map(lambda x,y:x+y, ismlar,familiyalar))
# print(ism_familiya)

# print(list(map(lambda matn: matn.title(),ismlar)))

# import random as r
# sonlar = r.sample(range(100),10)
# def juftmi(x):
#     return x%2==0


# juft_sonlar = list(map(lambda son: son%2==0,sonlar))
# print(sonlar)
# print(juft_sonlar)

# import random as r
# x = r.randint(10,20)
# print(x)

# ism = 'aiferfefefoioio'
# print(r.choice(ism))

# ism = ['a','b','c']
# r.shuffle(ism)
# print(ism)

# print(r.sample(ism,2))

# import random as r
# sonlar = list(r.sample(range(100),10))
# juft_sonlar = list(filter(lambda son: son%2==0,sonlar))

# print(sonlar)
# print(juft_sonlar)

# import random as r
# sonlar = list(r.sample(range(100),5))
# juft_sonlar = list(filter(lambda x: x%2==0, sonlar))

# print(sonlar)
# print(juft_sonlar)

# a = [1,2,3]
# b = [4,5,6]
# a_plus_b = list(map(lambda x,y: x+y, a,b))

# print(a_plus_b)

# mevalar = ['olma','banan','olcha','anor']
# mevaB = list(filter(lambda meva: meva.startswith('b'),mevalar))
# print(mevaB)

# mevalar = ['olma','anor','banan','bb']
# mevaB = list(map(lambda meva: meva.startswith('b'),mevalar))
# print(mevaB)

# mevalar1 = list(filter(lambda meva: (meva.startswith('b') and meva.endswith('n')),mevalar))
# print(mevalar1)

"""Amaliyot
180-bet
"""
# son = lambda x: x*10
# print(son(5))

# def daraja(n):
#     return lambda x: x**n

# kvadrat = daraja(2)
# kub = daraja(3)
# print(f"4 ning kvadraati {kvadrat(4)}, kubi {kub(4)}")

# yigindi = lambda x,y: x+y
# print(yigindi(14,14))

# import random as r
# sonlar = list(r.sample(range(1001),10))
# kvadratlari = list(map(lambda x: x*x,sonlar))
# toq_sonlar = list(filter(lambda x: x%2,sonlar))

# print(sonlar)
# print(kvadratlari)
# print(toq_sonlar)

# def tubmi(x):
#     if x%2==0 or x<2:
#         return False
#     if x==2 or x==3:
#         return True
#     for i in range(3,x,2):
#         if x%i==0:
#             return False
#     return True

# tub_sonlar = list(filter(tubmi,range(100)))
# print(tub_sonlar)

# print(all(x>5 for x in [6,7,8,4]))
# print(any([1,0,False]))
# scores = [20,10,80]
# print(any(score>40 for score in scores))

# a = ('name','age','year')
# b = ('alice','25')
# x = zip(a,b)
# print(list(x))

# x = range(5)
# print(list(x))

# x = None
# print(type(x))

# print(bool(1))

# def tubmi(x):
#     if x<2:
#         return False
#     if x==2 or x ==3 :
#         return True
#     for i in range(2,x):
#         if x%i == 0 :
#             return False
#     return True

# tub_sonlar = list(filter(tubmi, range(100)))
# print(tub_sonlar)

print("hello2")