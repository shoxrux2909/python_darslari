# DICTIONARY
# fanlar = {
#     'banana':20000,
#     'cherry':10000,
#     'grapes':30000,
#     "pineapple":25000
# }
# fanlar['apple']=10000
# fanlar['banana']=50000
# # print(fanlar)
# # print(fanlar.get("apple",'topilmadi'))
# arzon_mevalar = []
# for k,v in fanlar.items():
#     if v > 20000:
#         arzon_mevalar.append(k)
# print(arzon_mevalar)
# print(list(fanlar.keys()))
# print(list(fanlar.values()))

# SET, To'plam
# mevalar = {'olma','anor','olma','anor','nok'} # Unordered
# print(mevalar)
# print(mevalar)
# ERROR lar 
# IndexError
# my_list = [1,2,3,4]
# print(my_list[4])

# ZeroDivisionError
# x = 0
# y = 7
# print(y/x)

# TypeError
# x = 'a'
# y = 4
# print(x+y)

# try: harakat qilish, urinib ko'rmoq
# except: istisno, ..dan tashqari

# try:
#     print(7/0)
# except ZeroDivisionError:
#     pass
#     print("no'lga bo'lib bo'lmaydi")

# try:
#     x = 'a'
#     y = 5
#     print(x+y)
# except Exception as e:
#     print(e)
# else:
#     print("Men faqatgina try ishlasa sihlayman")
# finally:
#     print("Men har doim ishlayman, try niham\exceptni ham farqi yo'q")

# student_ortacha = {

# }

# students = {
#     'ali':[75,80,72,65],
#     'vali':[98,88,90,97],
#     'oysha':[56,60,58,70]
# }

# for key, value in students.items():
#     student_ortacha[key] = sum(value)//len(value)

# print(student_ortacha)
