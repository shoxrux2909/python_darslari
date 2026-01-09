# names = ['Sardor', 'Botir', 'Ahror']
# print("Birinchi ism:", names[0].title())
# print("Ikkinchi ism:", names[1].upper())

# narxlar = [12000, 18000, 30000]
# print(narxlar[2]-narxlar[1])
# print(narxlar[-1])

# narxlar = [12000, 40000, 56000]
# narxlar[0] = 12001
# narxlar[1] = 40001
# narxlar[2] = narxlar[2]+22
# print(narxlar)

# bozorlik = ["go'sht", 'kartoshka', 'sabzi']
# olindi = bozorlik.pop(1)
# print("Men " + olindi + " sotib oldim")
# print("Olinmagan mahsulotlar:", bozorlik)

# numbers = [1,2,3,4]
# print(numbers)
# numbers.pop()
# del numbers[1]
# print(numbers)

ismlar = ['Ali', 'Doni', 'Salim',]
print("Salom " + ismlar[0] + " ishlaring yaxshimi")
print(ismlar[1] + " va " + ismlar[2] + " qarindosh")

# sonlar = [1,-9,-8,11,2,11.4]
# print(sonlar[2]-sonlar[3])
# print(f"{sonlar[0]} - {sonlar[4]} = {sonlar[0]-sonlar[4]}")
# sonlar[1] = 0
# print(sonlar[2:4])

# t_shaxslar = ['Da vinchi', 'Rafael', 'Donatella']
# z_shaxslar = ['Chris Evans', "Mark Rufallo", "Scarslet Johnson"]
# print(f"Men tarixiy shaxslardan {t_shaxslar.pop(1)} ni\n\
# zamonaviy shaxslardan {z_shaxslar.pop(2)} ni ko'rishni hoxlardim    ")
# print(t_shaxslar)
# print(z_shaxslar)

# friend = []
# friend.append('Salim')
# friend.append('Nodir')
# friend.append('Zafar')
# print(friend)
# friend.remove('Zafar')
# print(friend)
# friend.insert(0,'Olim')
# friend.append("Alib")
# print(friend)
# mehmonlar = []
# mehmonlar.append(friend.pop(0))
# mehmonlar.append(friend.pop(1))
# print(friend)
# print(mehmonlar)

# cars = ['ferrari','audi','honda','bmw','Damas']
# cars.sort(reverse=True)
# print(cars)

# mehmonlar = ['Asilbek','Nodir','Abror']
# print("sorted() ro'yxat ko'rinishi: ", sorted(mehmonlar))
# print("Asl  ro'yxat: ", mehmonlar)

# ages = [25,12,45,11,56]
# ages.sort()
# print(ages)
# print(sorted(ages, reverse=True))

# fruits = ['Olma','Anor','Nok']
# fruits.reverse()
# print(fruits)
# print("Elementlar soni:", len(fruits))

# sonlar = list(range(0,10,2))
# sonlar2 = list(range(1,10,2))
# print("Juft sonlar :", sonlar)
# print("Toq sonlar :", sonlar2)

# narxlar = [12000,14000,32000,52000]
# min_narx = min(narxlar)
# max_narx = max(narxlar)
# sum_narxlar = sum(narxlar)
# print(
#     "Minimal narx :", min_narx, 
#     ". Maxsimal narx :", max_narx,
#     ". Jami narxlar :", sum_narxlar 
# )

# cars = ["audi",'ferrari','honda']
# my_cars = cars[1]
# print(my_cars)
# print(cars)
# cars2 = cars[:]
# cars2.append('bbb')
# cars2.append('gggg')
# print(cars2)

# toys = ('dragon','ritsar','car')
# toys = list(toys)
# toys[1] = 'drag'
# toys.append('boat')
# toys.remove('car')
# toys = tuple(toys)
# print(toys)

# mehmonlar = ['Ali','Vali','Doni']
# for mehmon in mehmonlar:
#     print(f"Hurmarli mehmon, {mehmon}")
#     print("Sizni to'y oqshomiga taklif etamiz!")
# print("Tugadi!!!")

# cars = ['nexia','damas','lasetti']
# for car in cars:
#     print(car.upper())

# sonlar = list(range(1,11))
# for son in sonlar:
#     print(f"Ushbu sonning {son} kvadrati : {son**2}")

# sonlar = list(range(1,11))
# sonlar_kv = []
# for son in sonlar:
#     sonlar_kv.append(son**2)
# print(sonlar)
# print(sonlar_kv)

# dostlar = []
# print("5 ta do'stizgizni ismini kiriting: ")
# for n in range(5):
#     dostlar.append(input(f"{n+1}-chi do'stingizni ismi: "))
# print(dostlar)

ismlar = ['Ali','vali','nodir','dilshod','zafar']
for xabar in ismlar:
    print("Salom, do'stim", xabar)
print("Kod", len(ismlar), "marta takrorlandi.")

# toq_sonlar = list(range(1,100,2))
# for son in toq_sonlar:
#     print(son**3)

# print("5 ta yoqtirgan kinolaringiz:")
# kinolar = []
# for kino in range(5):
#     kinolar.append(input(f"{kino+1}-chi kino nomi: "))
# print(kinolar)

# odamlar = int(input("Bugun uchrashgan odamlaringiz soni: "))
# uchrashilgan = []
# for odam in range(odamlar):
#     uchrashilgan.append(input(f"{odam+1}-chi odamning ismi: "))
# print(uchrashilgan)

# number1 = float(input("Birinchi sonni k: "))
# number2 = float(input("Ikkinchi sonni k: "))
# print(f"1-chi sonni 2-chi songa bo'lgandagi qoldiq: {number1%number2}")

# number1 = float(input("Birinchi sonni k: "))
# number2 = float(input("Ikkinchi sonni k: "))
# print(f"{number1} - {number2} = {number1-number2}")
# print(f"{number1} + {number2} = {number1+number2}")
# print(f"{number1} / {number2} = {number1/number2}")
# print(f"{number1} * {number2} = {number1*number2}")

