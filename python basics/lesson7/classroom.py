# dict_ = {
#     'ism':'Ali',
#     'familiya':'Valiyev',
#     'yosh':25,
#     'user_id':'2222222222'
# }
# if "user_id" in dict_:
#     print(dict_["user_id"])
# else:
#     dict_["user_id"] = "145452114"
#     print(dict_['user_id'])
# dict_1 = {
#     'ism':'Ali',
#     'familiya':'Valiyev',
#     'yosh':23,
#     'user_id':'2222222222'
# }
# for k,q in dict_.items():
#     if k in dict_1 and q in dict_1.values():
#         print("teng")
#     else: print("teng emas")

# dict_['yosh'] = 23
# del dict_['user_id']
# dict_['viloyati'] = 'Namangan'
# print(dict_)

# menyu = {
#     'osh':15000,
#     'salat':3000,
#     'somsa':15000,
#     'kabob':20000,
#     'tuxum':15000
# }

# while True:
#     buyurtma = input("Ovqat nomini kiriting: (chiqish uchun 'stop') ")
#     if buyurtma == "stop":
#         print("Osh bo'lsin!")
#         break
#     print(menyu.get(buyurtma,f"Bizda {buyurtma} yo'q."))
