# car = {"model":"ferrari","rang":"qizil"}
# print(car["model"])
# print(car["rang"])

# talaba = {"ism":"Murod","yosh":"20","t_yil":"2003"}
# print(f"{talaba["ism"].title()}, \
# {talaba["t_yil"]} - yilda tug'ilgan, \
# {talaba["yosh"]} yoshda")

# car = {
#     "make":"GM",
#     "model":"Malibu",
#     "color":"Black",
#     "year":"2020"
#     }
# narx = car.get("narx","Bunday kalit mavjut emas!")
# print(car[narx])

# talaba["kurs"] = 4
# talaba["fakultet"] = "informatika"
# print(talaba)

# car = {}
# car['model'] = 'Mezda 6'
# car['color'] = 'Red'
# car['price'] = 40000
# print(car)
# car['price'] = 50000
# print(car)
# del car['price']
# print(car)

"""Amaliyot"""

# otam = {'ism':'shuhrat jonuzoqov','t_yil':1975,'shahar':'Muborak'}
# print(f"Mening otam {otam['ism'].title()}, \
# {otam['shahar']} shahrida, \
# {otam['t_yil']}-yilda tug'ilganlar")

# ukam = {'ismi':'abbos','tyil':2008,'viloyat':'muborak'}
# tyil = ukam['tyil']
# vil = ukam['viloyat']
# print(f"Mening ukam {ukam['ismi'].title()} {tyil}-yilda {vil.title()} tug'ilgan")

# sevimli_taomlar = {'otam':'osh','onam':'somsa','ukam':'kabob'}
# print(f"Otamning sevimli taomi {sevimli_taomlar['otam']}, \
# Onamning sevimli taomi {sevimli_taomlar['onam']}")

# sevimli_taomlar = {
#     "amakim":"shashlik",
#     'tog\'am':'osh',
#     'bobom':'sho\'rva'
# }
# print(f"Amakimning sevimli taomi {sevimli_taomlar['amakim']}")

# izohli_lugat = {
#     'int':'int - butun sonlar',
#     'float':'float - o\'nlik sonlar',
#     'string':'string - matn',
#     'list':'list - ro\'yxat',
#     'tuple':'tuple - o\'zgarmas ro\'yxat',
#     'if':'if - agar operatori',
#     'else':'else - bo\'lmaganda operatori',
#     'elif':'elif - agarda bo\'lmasa operatori',
#     '==':'== - tenglash operatori',
#     '!=':'!= - teng emas operatori'}
# print(izohli_lugat)

# word = input("So'z kiriting: ")
# if word in izohli_lugat:
#       print(izohli_lugat[word])
# else: print(f"Bizda {word} so'zi mavjud emas!")

# kalit = input("So'z kiriting: ").lower()
# tarjima = izohli_lugat.get(kalit)
# if tarjima == None:
#     print(f"Bizda {kalit} so'zi mavjud emas!")
# else: print(f"{kalit} so'zining tarjimasi: {tarjima}")

# talaba = {
#     'ism':'alijon',
#     'familiya':'shamiyev',
#     'yosh':22,
#     'kurs':4
# }
# print(talaba.items())
# print(talaba.keys())
# print(talaba.values())
# for kalit, qiymat in talaba.items():
#     print(f"Kalit: {kalit}")
#     print(f"Qiymat: {qiymat}")

# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy 9',
#     'olim':'mi 90 pro',
#     'orif':'nokia',
#     'tesha':'nokia'
# }

# for k,q in telefonlar.items():
#     print(f"{k} ning telefon modeli {q}")

# for telefon in telefonlar.keys():
#     print(telefon.title())

# mahsulotlar = {
#     'olma': 40000,
#     'nok': 30000,
#     'uzum': 20000,
#     'anjir': 25000
# }

# bozorlik = ['olma','nok','shaftoli']
# for m in mahsulotlar:
#     if m in bozorlik:
#         print(f'{m.title()} {mahsulotlar[m]} so\'m')

# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"kechirasiz bizda {buyum} yo'q")

# print("Do'konimizdagi mahsulotlar:")
# for m in sorted(mahsulotlar):
#     print(m.title())

# print(mahsulotlar.values())

# print("Foydalanuvchilar telefonlari:")
# for tel in set(telefonlar.values()):
#     print(tel.title())

"""Amaliyot"""

# pyhton_izohli_lugat = {
#     'int':'int - butun sonlar',
#     'float':'float - o\'nlik sonlar',
#     'string':'string - matn',
#     'list':'list - ro\'yxat',
#     'tuple':'tuple - o\'zgarmas ro\'yxat',
#     'if':'if - agar operatori',
#     'else':'else - bo\'lmaganda operatori',
#     'elif':'elif - agarda bo\'lmasa operatori',
#     '==':'== - tenglash operatori',
#     '!=':'!= - teng emas operatori'}

# for k,q in sorted(pyhton_izohli_lugat.items()):
#     print(f"So'z: {k}, tarjima: {q}")

# for suz, tarjima in sorted(pyhton_izohli_lugat.items()):
#     print("So'z:", suz)
#     print("tarjima:", tarjima)

# davlat_poytaxt = {
#     'pakistan':'islamabad',
#     'new zealand':'wellington',
#     'italy':'rome',
#     'australia':'canberra'
# }

# print(sorted(davlat_poytaxt))
# print(sorted(davlat_poytaxt.values()))

# print("Davlat nomlari:")
# for davlat in davlat_poytaxt:
#     print(davlat.upper())

# print("Poytaxt nomlari:")
# for poytaxt in davlat_poytaxt.values():
#     print(poytaxt.title())

# davlat_nomi = input("Davlat nomini kiriting: ").lower()
# if davlat_nomi in davlat_poytaxt:
#     print(f"{davlat_nomi.upper()} poytaxti {davlat_poytaxt[davlat_nomi].title()}")
# else: print("Bizda bunday ma'lumot yoq!")

# davlat_nomi = input("Davlat nomini kiriting: ").lower()
# poytaxt = davlat_poytaxt.get(davlat_nomi)
# if poytaxt==None:
#     print(f"Bizda bunday ma'lumot yoq!")
# else: print(f"{davlat_nomi.title()} ning poytaxti {poytaxt.capitalize()} shahri.")

# menu = {
#     'osh':20000, 'sho\'rva':20000,
#     'somsa':15000, 'tuxum':15000,
#     'baliq':30000,
#     'kabob':30000,
#     'manti':25000
# }

# taomlar = []
# print("3 ta ovqat buyurtma bering:")
# for n in range(3):
#     taomlar.append(input(f"{n+1}-ovqatni kiriting: "))

# for taom in taomlar:
#     if taom in menu:
#         print(f"{taom.title()} narxi {menu[taom]} so'm")
#     else: print(f"Bizda {taom} yo'q!")

# menu = {
#     'osh':20000, 'sho\'rva':20000,
#     'somsa':15000, 'tuxum':15000,
#     'baliq':30000,
#     'kabob':30000,
#     'manti':25000
# }

# taomlar = []
# print("3 ta taom kiriting:")
# for n in range(3):
#     taomlar.append(input(f"{n+1}-taom: "))

# for taom in taomlar:
#     if taom in menu:
#         print(f"{taom} narxi {menu[taom]} so'm")
#     else:
#         print(f"Kechirasiz, Menyuda {taom} yo'q!")

# sonlar = {1,1,1,2,2,3,4}
# print(sonlar)

# mevalar = ['olma','nok','olma','olma','nok','behi']
# mevalar = set(mevalar)
# print(mevalar)
# mevalar = list(mevalar)
# print(mevalar)

# mevalar = {'olma','anor'}
# print(type(mevalar))
# mevalar.add('nok')
# print(mevalar)
# mevalar.update(['anjir'])
# print(mevalar)
# mevalar.discard('olma')
# mevalar.remove('anor')
# print(mevalar)

"""To'plamlar"""

# A = {1,2,3,4}
# B = {3,4,5,6}
# print(A.union(B))
# print(A&B)
# print(B.intersection(A))
# print(A-B)
# print(B.difference(A))
# print(B^A)
# print(B.symmetric_difference(A))

"""Amaliyot"""

# colors = {'red','green','blue'}
# colors.add('brown')
# colors.update(['silver'])
# print(colors)

# ranglar = {'qizil','qora','oq'}
# ranglar.update(['yashil','malla'])
# ranglar.add('ko\'k')
# print(ranglar)

# set1 = {10,20,30,40,50}
# set2 = {30,40,50,60,70}
# set3 = set1.union(set2)
# print(set3)

# A = {10,20,30,40,50}
# B = {30,40,50,60,70}
# C = A.union(B)
# print(C)

# print(set1.difference(set2))
# print(set2.difference(set1))

# print(set1.symmetric_difference(set2))

# bozorlik = ['choy','non','kartoshka','tuxum','sut']
# mahsulotlar = ['non','sut','tuxum','olma','un','tuz']
# bozorlik = set(bozorlik)
# mahsulotlar = set(mahsulotlar)
# bor_mahsulotlar = list(bozorlik.intersection(mahsulotlar))
# print(bor_mahsulotlar)

# yoq_mahsulotlar = list(bozorlik.difference(mahsulotlar))
# print(yoq_mahsulotlar)

# mahsulotlar.update(yoq_mahsulotlar)
# print(mahsulotlar)

# bozorlik = ['ruchka','qalam','daftar']
# mahsulotlar = ['qalam','kitob','sumka']
# bozorlik = set(bozorlik)
# mahsulotlar = set(mahsulotlar)
# # bor_mahsulotlar = bozorlik.intersection(mahsulotlar)
# # print(bor_mahsulotlar)

# yoq_mahsulotlar = bozorlik.difference(mahsulotlar)
# # print(yoq_mahsulotlar)
# print(mahsulotlar)
# yoq_mahsulotlar = list(yoq_mahsulotlar)
# mahsulotlar.update(yoq_mahsulotlar)
# print(mahsulotlar)

# savol = 'Istalgan sonni kiriting '
# savol += '(chiqish uchun \'exit\' deb yozing): '
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)

# savol = 'Istalgan sonni kiriting '
# savol += '(chiqish uchun \'exit\' deb yozing): '

# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break
#     elif qiymat == 'con':
#         continue
#     elif qiymat == '9':
#         pass  
#     else: print(float(qiymat)**2)

