# class Car:
#     brand = 'GM'

#     def __init__(self, year, price, color):
#         self.year = year
#         self.price = price
#         self.color = color

#     def __str__(self):
#         return f"{self.year}, {self.price}, {self.color}, {self.brand}"
    
#     def __repr__(self):
#         return f"Car year={self.year}, price={self.price}"
    
# obj1 = Car(2025,10000,'oq')
# obj2 = Car(2022,14000,'qizil')
# obj3 = Car(2020,8000,'qora')

# print(obj1)
# print(repr(obj1))
# print(obj1.color)

# class Car:
#     brand = 'GM'

#     def __init__(self, year, price, color, fuel):
#         self.year = year
#         self.price = price
#         self.color = color
#         self.is_engine_on = False
#         self.fuel = fuel

#     def __str__(self):
#         return f"{self.year}, {self.price}, {self.color}, {self.brand}"
    
#     def __repr__(self):
#         return f"Car year={self.year}, price={self.price}"
    
#     def star_engine(self):
#         if not self.is_engine_on:
#             self.is_engine_on = True
            
#             return f"Car is succesfully turned on"
#         return f"Car is already on"
    
#     def drive(self):
#         if self.is_engine_on:
#             return f"We are driving look at on your road"
#         return f"You should start engine on first"
    
#     def fuel_in_car(self):
#         return f"Fuel is enough for {100000//self.fuel} km"
    
# gentra = Car(2025,20000,"qora",20)
# print(gentra.star_engine())
# print(gentra.drive())
# print(gentra.star_engine())
# print(gentra.fuel_in_car())

