# with open('pi.txt') as fayl:
#     pi = fayl.read()
# print(pi)

# fayl = open('pi.txt')
# print(fayl.read())
# fayl.close()

# with open('pi.txt') as fayl:
#     pi = fayl.read()

# pi = pi.rstrip()
# pi = pi.replace("\n","")
# pi = float(pi)
# print(pi)

# with open('talabalar.txt') as fayl:
    # for line in fayl:
    #     print(line)
#     talabalar = fayl.readlines()
# talabalar = [talaba.rstrip() for talaba in talabalar]
# print(talabalar)

# faylnomi = 'Ustozlar.txt'
# with open(faylnomi, 'w') as fayl:
#     fayl.write("Hello World!")

# faylnomi = 'olimjon.txt'
# ism = 'Olimjon Hasanov'
# tyil = 2003
# with open(faylnomi, 'w') as fayl:
#     fayl.write(ism)
#     fayl.write(tyil)

# faylnomi = 'olimjon.txt'
# ism = 'Olimjon Husanov'
# tyil = 2003
# with open(faylnomi,'w') as fayl:
#     fayl.write(ism)
#     fayl.write(str(tyil))

# faylnomi = 'olimjon.txt'
# ism = 'Olimjon Hamrayev'
# tyil = 2003
# with open(faylnomi,'w') as fayl:
#     fayl.write(ism+'\n')
#     fayl.write(str(tyil)+'\n')

# with open(faylnomi,'a') as fayl:
#     fayl.write('Alijon Odilov\n')
#     fayl.write('2004\n')

import pickle

# talaba1 = {'ism':'ali','familiya':'alimov','tyil':'2003','kurs':'2'}
# talaba2 = {'ism':'vali','familiya':'valimov','tyil':'2003','kurs':'2'}
# talaba3 = {'ism':'sali','familiya':'salimov','tyil':'2003','kurs':'2'}

# with open('info','wb') as fayl:
#     pickle.dump(talaba1,fayl)
#     pickle.dump(talaba2,fayl)

# with open('info','rb') as fayl:
#     talaba1 = pickle.load(fayl)
#     talaba2 = pickle.load(fayl)

# print(talaba1,talaba2)

# with open('pi_million_digits.txt') as file:
#     pi_digits = file.read()

# pi_digits = pi_digits.rstrip()
# pi_digits = pi_digits.replace('\n','')
# pi_digits = pi_digits.replace(' ','')
# # print('9977' in pi_digits)
# print(pi_digits)
# pi_digits = float(pi_digits)
# print(pi_digits)
# with open('pi_folat.dat','wb') as file:
#     pickle.dump(pi_digits,file)

# with open('pi_folat.dat','rb') as file:
#     pi_digits = pickle.load(file)

# print(pi_digits)

# with open('pi_million_digits.txt') as file:
#     pi = file.read().strip()

# print(len(pi))
# print(pi[:50])
# while True:
#     faylnomi = 'info.txt'
#     ism = input("Ismingizni kiriting: ")
#     familiya = input("Familiyangizni kiriting: ")
#     tyil = input("Tug'ilgan yilingizni kiriting: ")

#     with open(faylnomi, 'a') as f:
#         f.write(ism+'\n')
#         f.write(familiya+'\n')
#         f.write(tyil+'\n')

#     javob = input("Yana ma'lumot kiritasizmi? (ha/yoq): ")
#     if javob == 'yoq':
#         break


