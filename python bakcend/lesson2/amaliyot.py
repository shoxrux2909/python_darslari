# """"Amaliyot 
# 210-bet
# """

# # class Shaxs:
# #     """Shaxs haqida ma'lumot"""
# #     def __init__(self, ism, familiya, passport, tyil):
# #         self.ism = ism
# #         self.familiya = familiya
# #         self.passport = passport
# #         self.tyil = tyil

# #     def get_info(self):
# #         info = f"{self.ism} {self.familiya},"
# #         info += f" Passport: {self.passport}, {self.tyil}-yilda tug'ilgan"
# #         return info
    
# #     def get_age(self, yil=2026):
# #         return f"{yil - self.tyil} yoshda"

# # inson = Shaxs('Ali','Valiyev',"AB121214",2003)
# # print(f"{inson.get_info()} {inson.get_age()}")

# # class Talaba(Shaxs):
# #     """Talaba klassi"""
# #     def __init__(self, ism, familiya, passport, tyil, id, manzil):
# #         super().__init__(ism, familiya, passport, tyil)
# #         self.idraqam = id
# #         self.bosqich = 1
# #         self.manzil = manzil
# #         self.fanlar = []

# #     def fan_yozil(self, fan):
# #         self.fanlar.append(fan)
# #         return self.fanlar
    
# #     def remove_fan(self, fan):
# #         if fan in self.fanlar:
# #             self.fanlar.remove(fan)
# #             return "Bu fan o'chirildi"
# #         return "Siz bu fanga yozilmagansiz"

# #     def get_idraqam(self):
# #         return self.idraqam
    
# #     def get_bosqich(self):
# #         return self.bosqich
    
# #     def get_info(self):
# #         info = f"{self.ism} {self.familiya}, "
# #         info += f"ID:{self.idraqam}, {self.bosqich}-bosqich talabasi"
# #         return info
    
# # talaba = Talaba("Vali","Valiyev","AB141414",2002, "00000014")
# # print(f"{talaba.get_info()}. ID: {talaba.get_idraqam()}")
# # print(f"{talaba.get_bosqich()}-bosqich talabasi")
# # print(talaba.get_info())

# # class Manzil:
# #     """Manzil klassi"""
# #     def __init__(self, uy, kocha, tuman, viloyat):
# #         self.uy = uy
# #         self.kocha = kocha
# #         self.tuman = tuman
# #         self.viloyat = viloyat

# #     def get_manzil(self):
# #         manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
# #         manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
# #         return manzil
    
# # manzil = Manzil(26,"Alisher Navoiy","Olmazor","Samarqand")
# # talaba = Talaba("Ali","Valiyev","AB141414",2003,"00000014",manzil)

# # print(talaba.manzil.tuman)

# # class Fan:
# #     """Fan klassi"""
# #     def __init__(self, name, code, teacher, room):
# #         self.name = name
# #         self.code = code
# #         self.teacher = teacher
# #         self.room = room

# #     def __repr__(self):
# #         return f"{self.name} ({self.code})"

# # math = Fan("math", "MAH101", "ALiyev", 23)
# # english = Fan('English',"ENG202","Valiyev", 24)
# # talaba = Talaba("Vali","Valiyev","AB141414",2002, "00000014", manzil)
# # talaba.fan_yozil(math)
# # talaba.fan_yozil(english)

# # print(talaba.fanlar)
# # talaba.remove_fan(math)
# # print(talaba.fanlar)

# # class User(Shaxs):
# #     """Foydalanuvchi klassi"""
# #     def __init__(self, ism, familiya, passport, tyil, email):
# #         super().__init__(ism, familiya, passport, tyil)
# #         self.email = email
    
# #     def get_email(self):
# #         return self.email
    
# #     def get_info(self):
# #         return f"{self.ism}, {self.email}"

# # talaba1 = User("a","b","v","2002","email.com")
# # print(talaba1.get_info())

# from uuid import uuid4
# class Avto:
#     """Avtomobil klassi"""
#     __num_auto = 0
#     def __init__(self, make, model, rang, yil, narx, km=0):
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narx = narx
#         self.__km = km
#         self.__id = uuid4()
#         Avto.__num_auto += 1

#     def get_km(self):
#         return self.__km
    
#     def get_id(self):
#         return self.__id
    
#     def add_km(self,km):
#         if km>=0:
#             self.__km += km
#         else:
#             return "Mashina km kamaytirib bo'lmaydi" 
    
#     def __repr__(self):
#         return f"{self.model} {self.narx} {self.rang}"
    
#     def __eq__(self, boshqa_avto):
#         return self.narx == boshqa_avto.narx
    
#     def __lt__(self, boshqa_avto):
#         return self.narx<boshqa_avto.narx
    
#     def __le__(self, boshqa_avto):
#         return self.narx<=boshqa_avto.narx
        
#     @classmethod
#     def get_num_avto(cls):
#         return cls.__num_auto
    
# auto1 = Avto("GM",'cobalt','qizil',2020,12000,100000)
# auto2 = Avto("GM",'nexia','qizil',2020,20000,100000)
# auto3 = Avto("GM",'nexia','yashil',2020,30000,100000)
# # print(auto1>auto2)

# class AvtoSalon:
#     """Avtosalon klassi"""
#     def __init__(self, name):
#         self.name = name
#         self.avtolar = []

#     def __repr__(self):
#         return f"{self.name} avtosaloni"
    
#     def __len__(self):
#         return len(self.avtolar)
    
#     def __getitem__(self, index):
#         return self.avtolar[index]
    
#     def __setitem__(self, index, value):
#         if isinstance(value, Avto):
#             self.avtolar[index]=value

#     def __call__(self, *args):
#         if args:
#             for avto in args:
#                 self.add_auto(avto)
#         else: 
#             return [auto for auto in self.avtolar]
        
#     def add_auto(self, *qiymat):
#         for auto in qiymat:
#             if isinstance(auto,Avto):
#                 self.avtolar.append(auto)
#             else: print("Avto obyektini kiriting!")
    
# # salon1 = AvtoSalon("MaxAuto")
# # print(salon1)
# # print(isinstance("salom",int))
# # print(isinstance(95,int))
# # print(isinstance(auto1,Avto))

# # for auto in [auto1,auto2,auto3]:
# #     salon1.add_auto(auto)

# # print(len(salon1))
# # print(salon1[0])
# # print(salon1[:])
# # auto4 = Avto('GM','damas','oq',2022,15000,100000)
# # salon1[0]=auto4
# # print(salon1[0])
# salon1 = AvtoSalon('MaxAuto')
# salon2 = AvtoSalon('MaxAuto2')
# auto1 = Avto('GM','nexia','oq',2023,15000,100000)
# auto2 = Avto('GM','nexia','qizil',2023,15000,100000)
# auto3 = Avto('GM','nexia','qora',2023,15000,100000)
# auto4 = Avto('GM','nexia','yashil',2023,15000,100000)
# auto5 = Avto('GM','nexia','sariq',2023,15000,100000)
# auto6 = Avto('GM','nexia','kumush',2023,15000,100000)
# salon1.add_auto(auto1,auto2,auto3)
# salon2.add_auto(auto4,auto5,auto6)

# # salon1+salon2
# # print(salon1())
# avto7 = Avto('GM','lasetti','oq',2023,17000)
# salon1(avto7)
# print(salon1())