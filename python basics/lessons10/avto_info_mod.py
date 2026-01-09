def avto_info(make,model,rangi,korobka,yili,narxi=None):
    avto = {
        "kompaniya":make,
        'model':model,
        'rang':rangi,
        'korobka':korobka,
        'yil':yili,
        'narx':narxi
    }
    return avto

def avto_kirit():
    """Foydalanuvchiga avto_info funksiyasi yordamida 
     bir nechta avtolar haqida ma'lumotlarni bitta 
    ro'yxatga joylash imkonini beruvchi funksiya """
    avtolar = []
    while True:
        print("\nQuyidagi ma'lumotlarni kiriting:", end='')
        make = input("Ishlab chiqaruvchi: ")
        model = input("Modeli: ")
        rangi = input("Rangi: ")
        korobka = input("Korobka: ")
        yili = input("Ishlab chiwarilgan yili: ")
        narxi = input("Narxi: ")
        avtolar.append(avto_info(make,model,rangi,korobka,yili,narxi))
        
        javob = input("Yana avto kiritasizmi? yes/no : ")
        if javob == "no":
            break
    return avtolar

def info_print(avto_info):
    """Avtomobillar haqida ma'lumotlar 
    saqlangan lug'atni konsolga chiqarish"""
    print(f"{avto_info['rang'].title()} "
          f"{avto_info['kompaniya'].upper()} "
          f"{avto_info['model'].upper()}, "
          f"{avto_info['korobka'].title()}, "
          f"{avto_info['yil']}-yil, {avto_info['narx']}$")