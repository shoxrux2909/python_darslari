"""inputga 20 ta misol"""

# ism = input("Ismingizni kiriting: ")
# print("Salom,", ism)

# son = float(input("Istalgan sonni kiriting: "))
# print("Siz tanlagan son:", son)

# butun_son = int(input('Butun son kiriting: '))
# print("Butun son:", butun_son) 

# meva = input("Meva nomini kiriting: ")
# print("Siz kiritgan meva nomi:", meva)

# raqam = int(input("Raqam kiriting: "))
# print("Siz kiritgan raqam:", raqam)

# son = float(input(f"Istalgan sonni kiriting: "))
# print(f"Siz tanlagan son: {son}")

# son2 = float(input('Son kiriting: '))
# print("Sonning kubi:", son2**3)

# meva1 = input("Meva nomini kiriting: ")
# print("Siz kiritgan meva nomi katta harflarda:", meva1.upper())

# ism1 = input("Ismingizni kiriting: ")
# print("Siz kiritgan ism kichik harflarda", ism1.lower())

# son2 = float(input("Istalgan sonni kiriting: "))
# print(son2, "ni 9 ga bo'linmasi:", son2/9)

# son3 = float(input('Son kiriting: '))
# print(son3, "ning 6 ga ko'paytmasi:", son3*6) 

# meva = input("Meva nomini kiriting: ")
# print("Men", meva, "ni yaxshi ko'raman")

# ism = input("Ismingizni kiriting: ")
# print("Mening ismim", ism)

# son4 = float(input("Istalgan sonni kiriting: "))
# print(f"{son4} ni 5 ga bo'lgandagi qoldiq: {son4%5}")

# son5 = float(input('Son kiriting: '))
# print(son5, "ni 7 ga bo'lgandagi butun qismi:", son5//7) 

# meva5 = input("Meva nomini kiriting: ")
# print("Meva nomining bosh harfi kattada:", meva5.title())

# ism5 = input("Do'stingizni ismini kiriting: ")
# print("Mening do'stim " + ism5)

# son6 = float(input("Istalgan sonni kiriting: "))
# print(f"{son6} ning 7 ga ayirmasi: {son6-7}")

# birthyear = int(input('Tug\'ilgan yilingizni kiriting: '))
# print("Siz", 2025-birthyear, "yoshdasiz") 

# car = input("Avtomobil nomini kiriting: ")
# print("Siz kiritgan Avtomobile "  + car + " deb nomlanadi.")

"""kalkulyatorga 5ta amalga misol ishlash"""

# son1 = float(input("Birinchi sonni kiriting: "))
# son2 = float(input("Ikkinchi sonni kiriting: "))
# print(f"{son1} va {son2} yi'gindisi: {son1+son2}")

# son1 = float(input("Birinchi sonni kiriting: "))
# son2 = float(input("Ikkinchi sonni kiriting: "))
# print(f"{son1} va {son2} ayirmasi: {son1-son2}")

# son1 = float(input("Birinchi sonni kiriting: "))
# son2 = float(input("Ikkinchi sonni kiriting: "))
# print(f"{son1} va {son2} bo'linmasi: {son1/son2}")

# son1 = float(input("Birinchi sonni kiriting: "))
# son2 = float(input("Ikkinchi sonni kiriting: "))
# print(f"{son1} va {son2} bo'lgandagi qoldiq: {son1%son2}")

# son1 = float(input("Birinchi sonni kiriting: "))
# son2 = float(input("Ikkinchi sonni kiriting: "))
# print(f"{son1} va {son2} bo'linmasining butun qismi: {son1//son2}")

"""Ro'yxatga doir amaliyot"""


# ismlar = ['Ali', 'Doni', 'Salim']
# print("Salom " + ismlar[0] + " ishlaring yaxshimi")
# print(ismlar[1] + " va " + ismlar[2] + " qarindosh")

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

# davlatlar = ["AQSH","Kanada","Yangi Zelandiya","Germaniya"]
# print(davlatlar)
# print(len(davlatlar))
# print(sorted(davlatlar))
# print(sorted(davlatlar, reverse=True))
# davlatlar.reverse()
# print(davlatlar)
# davlatlar.sort()
# print(davlatlar)
# davlatlar.sort(reverse=True)
# print(davlatlar)

# juft_sonlar = list(range(120,1200,2))
# print(sum(juft_sonlar))
# print(max(juft_sonlar)-min(juft_sonlar))
# print(len(juft_sonlar))
# print(juft_sonlar[:20])
# print(juft_sonlar[-20:])
# print(juft_sonlar[260:280])

# taomlar = ['somsa','manti','osh','makaron','tuxum']
# nonushta = taomlar[:]
# nonushta.remove('osh')
# nonushta.remove('manti')
# nonushta.remove('makaron')
# nonushta.append('sut')
# nonushta = tuple(nonushta)
# print(taomlar)
# print(nonushta)

# dostlar = []
# print("5 ta do'stizgizni ismini kiriting: ")
# for n in range(5):
#     dostlar.append(input(f"{n+1}-chi do'stingizni ismi: "))
# print(dostlar)

# ismlar = ['Ali','vali','nodir','dilshod','zafar']
# for xabar in ismlar:
#     print("Salom, do'stim", xabar)
# print("Kod", len(ismlar), "marta takrorlandi.")

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