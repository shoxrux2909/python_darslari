# car0 = {
#     'model':'lacetti', 'color':'red',
#     'year':2018, 'price':13000,
#     'km':50000,'korobka':'avtomatika'
# }
# car1 = {
#     'model':'nexia 3', 'color':'black',
#     'year':2015, 'price':9000,
#     'km':89000,'korobka':'mexanika'
# }
# car2 = {
#     'model':'gentra', 'color':'white',
#     'year':2019, 'price':15000,
#     'km':20000,'korobka':'mexanika'
# }
# cars = [car0,car1,car2]
# for car in cars:
#     print(f"{car['model'].title()}, "
#           f"{car['color']} rang, "
#           f"{car['year']}-yil, {car['price']}$")

# dasturchilar = {
#     'ali':['python','css','c++'],
#     'vali':['c++','java']
# }
# for ism,tillar in dasturchilar.items():
#     print(f"\n{ism.title()}: ", end='')
#     for til in tillar:
#         print(f"{til.upper()} ", end='')
"""Amaliyot"""
# person0 = {
#     'name':'abu abdulloh', 'surname':'ibn ismoil',
#     'b_year':830, 'region':'buxoro'
# }
# person1 = {
#     'name':'abdulla', 'surname':'qodiriy',
#     'b_year':1894, 'region':'toshkent'
# }
# person2 = {
#     'name':'erkin', 'surname':'vohidov',
#     'b_year':1936, 'region':"farg'ona"
# }
# person3 = {
#     'name':'alisher', 'surname':'navoiy',
#     'b_year':1441, 'region':'xirotda'
# }

# people = [person0,person1,person2,person3]
# for person in people:
#     print(f"\n{person['name'].title()} {person['surname'].title()} {person['b_year']}-yilda ", end=
#           f"{person['region'].title()}da tavallud topgan.")

# buxoriy = {
#     'ism':'Abu Abdulloh Muxammad Ismoil',
#     'tyil':810,
#     'vyil':870,
#     'viloyat':'Buxoro',
#     'asarlari':['Al-adab','al-mufrad',
#                 'At-tarix','alkabir',
#                 'At-tarix',"as-sag'ir"]
# }
# qodiriy = {
#     'ism':'Abdulla Qodiriy',
#     'tyil':1894,
#     'vyil':1938,
#     'viloyat':'Toshkent',
#     'asarlari':["o'tkan kunlar",
#                 'Mehrobdan Chayon',
#                 'Obid Ketmon']
# }
# vohidiy = {
#     'ism':'Erkin Vohidov',
#     'tyil':1936,
#     'vyil':2016,
#     'viloyat':"Farg'ona",
#     'asarlari':['Tong nafasi',
#                 "Qo'shiqlarim sizga",
#                 "O'zbegim"]
# }
# shaxslar = [buxoriy,qodiriy,vohidiy]
# for shaxs in shaxslar:
#     ism = shaxs['ism']
#     tyil = shaxs['tyil']
#     vyil = shaxs['vyil']
#     tjoy = shaxs['viloyat']
#     print(f"{ism} {tyil}-yilda {tjoy}da tug'ilgan,",
#           f"{vyil-tyil} yil umr ko'rgan")

# for shaxs in shaxslar:
#     ism = shaxs['ism']
#     asarlar = shaxs['asarlari']
#     print(f"{ism} ning mashxur asarlari:")
#     for asar in asarlar:
#         print(asar)

# friend0 = {
#     'ism':'Donyor',
#     "kinolar":['Qasoskorlar',"Taxtlar o'yini"]
# }
# friend1 = {
#     'ism':'Nodir',
#     "kinolar":['Uzuklar hukmdori',"G'alati narsalar"]
# }
# friend2 = {
#     'ism':'Sardor',
#     "kinolar":['Avatar',"U.Derbyga xush kelibsiz!"]
# }
# friends = [friend0,friend1,friend2]
# for friend in friends:
#     ism = friend['ism']
#     kinolar = friend['kinolar']
#     print(f"{ism} ning yoqtirgan kinolari:")
#     for kino in kinolar:
#         print(kino)

# davlatlar = {
#     "o'zbekiston":{'poytaxt':"toshkent",
#                    'maydon':448978,
#                    'aholi':35_000_000,
#                    'pul birligi':"so'm"
#                    },
#     "koreya":{'poytaxt':'seoul',
#               'maydon':3625411,
#               'aholi':345_440_411,
#               'pul birligi':'won'},
#     'aqsh':{'poytaxt':"vashington",
#                 'maydon':9_631_418,
#                 'aholi':345_457_000,
#                 'pul birligi':"dollar"}
# }

# for davlat,info in davlatlar.items():
#     print(f"\n{davlat.title()}ning poytaxti {info['poytaxt'].title()}\
#     \nHududi: {info['maydon']} kv.km\
#     \nAholisi: {info['aholi']}\
#     \nPul birligi: {info['pul birligi']}")

# davlat_nomi = input("Davlat nomini k: ").lower()
# if davlat_nomi in davlatlar:
#     info = davlatlar[davlat_nomi]   
#     if davlat_nomi == 'aqsh':
#         davlat_nomi = davlat_nomi.upper()
#     else: davlat_nomi = davlat_nomi.capitalize()
#     print(f"\n{davlat_nomi}ning poytaxti {info['poytaxt'].title()}\
#         \nHududi: {info['maydon']} kv.km\
#         \nAholisi: {info['aholi']}\
#         \nPul birligi: {info['pul birligi']}")
# else:
#     print(f"Bizda {davlat_nomi} haiqda ma'lumot yo'q.")

# son = 0
# while son<10:
#     son += 1
#     if son%2 != 0:
#         continue
#     else:
#         print(son, end="")

# n = 1
# while n<6:
#     print(n, end="")
#     n += 1
"""Amaliyot"""

# while True:
#     kitob = input("Yaxshi ko'rgan kitobingizni k: ")
#     if kitob == 'stop':
#         break

# savol = "Yoshingizni kiriting:"
# savol += "(chiqish uchun 'exit' yoki 'quit' deb yozing!): "

# while True:
#     qiymat = (input(savol))
#     if qiymat == 'exit' or qiymat == 'quit':
#         break
#     else: yosh = int(qiymat)
#     if yosh<=7:
#         print("Chipta 2000 so'm")
#     elif yosh>7 and yosh<=18:
#         print("Chipta 3000 so'm")
#     elif yosh>18 and yosh<=65:
#         print("Chipta 10000 so'm")
#     else: print("Chipta bepul")

# savol = "Yoshingizni kiriting: "

# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit' or qiymat == "quit":
#         break
#     else: yosh = int(qiymat)
#     if yosh<7:
#         narx = 2000
#     elif 7<=yosh<18:
#         narx = 3000
#     elif 18<=yosh<65:
#         narx = 10000
#     else: narx = 0
#     if narx == 0:
#         print("Sizga chipta bepul")
#     else: print(f"Chipta {narx} so'm")

# savol = "Kiritilgan sonning ildizini qaytaruvchi dastur!\n"
# savol += "Musbat son kiriting "
# savol +="(dasturni to'xtatish uchun 'exit' deb yozing!): "

# while True:
#     qiymat = input(savol)
#     if float(qiymat)<0:
#         continue
#     elif qiymat == 'exit':
#         break
#     else:
#         ildiz = float(qiymat)**0.5
#         print(f"{qiymat} ning ildizi {ildiz} ga teng.")

# ismlar = []
# print("Yaqin do'stlaringiz ro'yxatini tuzmiz.")
# n = 1
# while True:
#     savol = f"{n}-do'stingiz ismini kiriting: "
#     ismlar.append(input(savol))
#     javob = input("Yana ism qo'shasizmi? (ha/yo'q) ")
#     if javob == 'ha':
#         n += 1
#         continue
#     else: 
#         break
# print("Ro'yxat tuzildi.")

# print("Do'stlaringiz ro'yxati:")
# for ism in ismlar:
#     print(ism.title())

# print("Do'stlaringiz yoshini saqlaymiz.")
# dostlar = {}
# ishora = True
# while ishora:
#     ism = input("Do'stingizni ismini kiriting: ")
#     yosh = input(f"{ism.title()}ning yoshini kiriting: ")
#     dostlar[ism] = int(yosh)

#     javob = input("Yana ma'lumot kiritasizmi? (ha/yo'q) ")
#     if javob == "yo'q":
#         ishora = False

# for ism, yosh in dostlar.items():
#     print(f"{ism.title()}ning yoshi {yosh} da")

# cars = ['nexia','lasetti','cobalt','nexia']
# while 'nexia' in cars:
#     cars.remove('nexia')
# print(cars)

# talabalar = ['hasan','husan','ali','vali']
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba.title()}ning bahosini kiriting: ")
#     print(f"{talaba.title()} baholandi.")
#     baholangan_talabalar[talaba] = baho

# for ism, ball in baholangan_talabalar.items():
#     print(f"{ism.title()}ning bahosi {ball} ga teng.")

# ruyxat = []
# while True:
#     mahsulot = input("Mahsulot nomini kiriting: ")
#     ruyxat.append(mahsulot)
#     qiymat = input("Yana ma'lumot kiritasizmi? (ha/yo'q) ")
#     if qiymat == "yo'q":
#         break
# print(ruyxat)

# e_bozor = {}
# while True:
#     mahsulot = input("Mahsulot nomini kiriting: ")
#     narx = int(input(f"{mahsulot}ning narxini kiriting: "))
#     e_bozor[mahsulot] = narx
#     qiymat = input("Yana ma'lumot kiritasizmi? (ha/yo'q) ")
#     if qiymat == "yo'q":
#         break
# print(e_bozor)

# buyurtmalar = ['olma','nok','behi','anjir']
# mahsulotlar = {
#     'nok':20000,
#     'behi':15000,
#     'olma':14000,
#     'anor':18000
# }
# for buyurtma in buyurtmalar:
#     if buyurtma in mahsulotlar:
#         narx = mahsulotlar[buyurtma]
#         print(f"{buyurtma}ning naxi {narx} so'm")
#     else: print(f"Bizda {buyurtma} mavjud emas.")

# while buyurtmalar:
#     buyurtma = buyurtmalar.pop()
#     if buyurtma in mahsulotlar:
#         narx = mahsulotlar[buyurtma]
#         print(f"{buyurtma.title()} - {narx} so'm")
#     else: print(f"Bizda {buyurtma} mavjud emas.")


