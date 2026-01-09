# class Student:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self, ism, familiya, tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil

# talaba1 = Student("Alijon","Sobiyev",2003)
# print(talaba1.ism)
# print(talaba1.familiya)

# class Student:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self, ism, familiya, tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
    
#     def tanishtir(self):
#         return (f"Ismim {self.ism} {self.familiya}."
#               f" {self.tyil}-yilda tug'ilganman")
    
#     def get_name(self):
#         return self.ism
    
#     def get_lastname(self):
#         return self.familiya
    
#     def get_fullname(self):
#         return f"{self.ism} {self.familiya}"

#     def get_age(self, yil):
#         return yil - self.tyil
      
# talaba1 = Student("Alijon","Sobiyev",2003)
# print(talaba1.ism)
# print(talaba1.familiya)
# print(talaba1.tanishtir())
# print(talaba1.get_fullname())
# print(talaba1.get_lastname())
# print(talaba1.get_age(2026))

"""Amaliyot
198-bet
"""
# class User:
#     """User nomli klass yaratamiz"""
#     def __init__(self, user_id, username, email):
#         self.user_id = user_id
#         self.username = username
#         self.email = email

#     def get_info(self):
#         return (f"Foydalanuvchi: {self.user_id} "
#                 f"ismi: {self.username} "
#                 f"email: {self.email}")
    
# user1 = User("aliyev2525",'Aliyev Botir',"aliyevbotir2003@gmail.com")
# user2 = User("valiyev2525",'Valiyev Botir',"valiyevbotir2003@gmail.com")
# user3 = User("doniyev2525",'Doniyev Botir',"doniyevbotir2003@gmail.com")
# print(user1.get_info())
# print(user2.email)
# print(user3.user_id)

# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self, ism, familiya, tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.bosqich = 1

#     def get_info(self):
#         return f"{self.ism} {self.familiya} {self.bosqich}-bosqich talabasi"
    
#     def set_bosqich(self, bosqich):
#         self.bosqich = bosqich
#         return self.bosqich
    
#     def update_bosqich(self):
#         self.bosqich += 1

# talaba1 = Talaba("Ali","Valiyev",2002)
# talaba1 = Talaba("Akrom","Valiyev",2003)
# talaba1 = Talaba("Aziz","Valiyev",2004)
# talaba1.update_bosqich()
# # talaba1.bosqich = 3
# print(talaba1.get_info())
# talaba1.update_bosqich()
# print(talaba1.get_info())

# class Fan():
#     def __init__(self, nomi):
#         self.nomi = nomi
#         self.talabalar_soni = 0
#         self.talabalar = []

#     def add_students(self, talaba):
#         self.talabalar_soni += 1
#         self.talabalar.append(talaba)

#     def get_studens(self):
#         return [talaba.get_info() for talaba in self.talabalar]

# talaba1 = Talaba("Ali","Valiyev",2002)
# talaba2 = Talaba("Akrom","Valiyev",2003)
# talaba3 = Talaba("Aziz","Valiyev",2004)

# matematika = Fan("Oliy matematiak")
# matematika.add_students(talaba1)
# matematika.add_students(talaba2)
# matematika.add_students(talaba3)

# print(matematika.talabalar_soni)
# mat_talabalar = matematika.get_studens()
# # print(mat_talabalar)

# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self, ism, familiya, tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.bosqich = 1

#     def set_bosqich(self, bosqich):
#         self.bosqich = bosqich
    
#     def update_bosqich(self):
#         self.bosqich += 1

#     def get_info(self):
#         return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi"

#     def get_name(self):
#         return self.ism

#     def get_lastname(self):
#         return self.familiya

#     def get_fullname(self):
#         return f"{self.ism} {self.familiya}"

#     def get_age(self, yil):
#         return yil - self.tyil

# class Fan():
#     def __init__(self, nomi):
#         self.nomi = nomi
#         self.talabalar_soni = 0
#         self.talabalar = []
    
#     def add_student(self, talaba):
#         self.talabalar.append(talaba)
#         self.talabalar_soni += 1

#     def get_name(self):
#         return self.nomi
    
#     def get_students(self):
#         return [x.get_info() for x in self.talabalar]

#     def get_student_num(self):
#         return self.talabalar_soni


# def see_methods(klass):
#     return [method for method in dir(klass) \
#             if method.startswith('__') is False]

# # print(see_methods(Talaba))
# talaba1 = Talaba("Ali","Valiytev",2003)
# talaba2 = Talaba("Vali","Aliyev",2002)
# talaba3 = Talaba("Doni","Aliyev",2000)  

# matematika = Fan("Oliy Matematika")
# matematika.add_student(talaba1)
# matematika.add_student(talaba2)
# matematika.add_student(talaba3)

# print(see_methods(talaba1))
# print(talaba1.__dict__)
# mat_talabalar = matematika.get_students()
# print(mat_talabalar)
# print(matematika.get_student_num())

# print(dir(Talaba))

class Avto:
    """Avto klasini yaratamiz"""
    def __init__(self, model, rang, korobka, narx):
        self.model = model
        self.rang = rang
        self.korobka = korobka
        self.narx = narx
        self.kilometer = 0

    def get_model(self):
        return self.model
    
    def get_rang(self):
        return self.rang
    
    def get_narx(self):
        return self.narx
    
    def get_info(self):
        return f"{self.model}, {self.korobka}, {self.narx}"
    
    def update_km(self, km):
        self.kilometer = km

class Avtosalon():
    def __init__(self, salon_nomi, manzili):
        self.nomi = salon_nomi
        self.manzil = manzili
        self.avtolar_soni = 0
        self.sotuvdagi_avtolar = []

    def add_avtos(self, avto):
        self.sotuvdagi_avtolar.append(avto)
        self.avtolar_soni += 1

    def get_avtos(self):
        return [x.get_info() for x in self.sotuvdagi_avtolar]

Avtosalon11 = Avtosalon("WWW","Qarshi viloyati")

avto1 = Avto('nexia','qora','korobka',25000)    
avto2 = Avto('kobalt','qora','korobka',20000)    
avto3 = Avto('damas','oq','korobka',14000)  

Avtosalon11.add_avtos(avto1)
Avtosalon11.add_avtos(avto2)
Avtosalon11.add_avtos(avto3)

# bor_avtolar = Avtosalon11.get_avtos()
# print(bor_avtolar)

# print(avto1.__dict__.values())