""""Amaliyot 
210-bet
"""

# class Shaxs:
#     """Shaxs haqida ma'lumot"""
#     def __init__(self, ism, familiya, passport, tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.passport = passport
#         self.tyil = tyil

#     def get_info(self):
#         info = f"{self.ism} {self.familiya},"
#         info += f" Passport: {self.passport}, {self.tyil}-yilda tug'ilgan"
#         return info
    
#     def get_age(self, yil=2026):
#         return f"{yil - self.tyil} yoshda"

# inson = Shaxs('Ali','Valiyev',"AB121214",2003)
# print(f"{inson.get_info()} {inson.get_age()}")

# class Talaba(Shaxs):
#     """Talaba klassi"""
#     def __init__(self, ism, familiya, passport, tyil, id, manzil):
#         super().__init__(ism, familiya, passport, tyil)
#         self.idraqam = id
#         self.bosqich = 1
#         self.manzil = manzil
#         self.fanlar = []

#     def fan_yozil(self, fan):
#         self.fanlar.append(fan)
#         return self.fanlar
    
#     def remove_fan(self, fan):
#         if fan in self.fanlar:
#             self.fanlar.remove(fan)
#             return "Bu fan o'chirildi"
#         return "Siz bu fanga yozilmagansiz"

#     def get_idraqam(self):
#         return self.idraqam
    
#     def get_bosqich(self):
#         return self.bosqich
    
#     def get_info(self):
#         info = f"{self.ism} {self.familiya}, "
#         info += f"ID:{self.idraqam}, {self.bosqich}-bosqich talabasi"
#         return info
    
# talaba = Talaba("Vali","Valiyev","AB141414",2002, "00000014")
# print(f"{talaba.get_info()}. ID: {talaba.get_idraqam()}")
# print(f"{talaba.get_bosqich()}-bosqich talabasi")
# print(talaba.get_info())

# class Manzil:
#     """Manzil klassi"""
#     def __init__(self, uy, kocha, tuman, viloyat):
#         self.uy = uy
#         self.kocha = kocha
#         self.tuman = tuman
#         self.viloyat = viloyat

#     def get_manzil(self):
#         manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
#         manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
#         return manzil
    
# manzil = Manzil(26,"Alisher Navoiy","Olmazor","Samarqand")
# talaba = Talaba("Ali","Valiyev","AB141414",2003,"00000014",manzil)

# print(talaba.manzil.tuman)

# class Fan:
#     """Fan klassi"""
#     def __init__(self, name, code, teacher, room):
#         self.name = name
#         self.code = code
#         self.teacher = teacher
#         self.room = room

#     def __repr__(self):
#         return f"{self.name} ({self.code})"

# math = Fan("math", "MAH101", "ALiyev", 23)
# english = Fan('English',"ENG202","Valiyev", 24)
# talaba = Talaba("Vali","Valiyev","AB141414",2002, "00000014", manzil)
# talaba.fan_yozil(math)
# talaba.fan_yozil(english)

# print(talaba.fanlar)
# talaba.remove_fan(math)
# print(talaba.fanlar)

# class User(Shaxs):
#     """Foydalanuvchi klassi"""
#     def __init__(self, ism, familiya, passport, tyil, email):
#         super().__init__(ism, familiya, passport, tyil)
#         self.email = email
    
#     def get_email(self):
#         return self.email
    
#     def get_info(self):
#         return f"{self.ism}, {self.email}"

# talaba1 = User("a","b","v","2002","email.com")
# print(talaba1.get_info())

from uuid import uuid4
class Avto:
    """Avtomobil klassi"""
    __num_auto = 0
    def __init__(self, make, model, rang, yil, narx, km=0):
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narx = narx
        self.__km = km
        self.__id = uuid4()
        Avto.__num_auto += 1

    def get_km(self):
        return self.__km
    
    def get_id(self):
        return self.__id
    
    def add_km(self,km):
        if km>=0:
            self.__km += km
        else:
            return "Mashina km kamaytirib bo'lmaydi" 
        
    @classmethod
    def get_num_avto(cls):
        
    
auto1 = Avto("GM","nexia","qizil",2010,15000,100000)
auto2 = Avto("GM","ccobalt","qizil",2010,15000,100000)
auto3 = Avto("GM","damas","qizil",2010,15000,100000)
# print(f"ID:{auto1.get_id()}")
# auto1.add_km(11005)
# print(auto1.get_km())
