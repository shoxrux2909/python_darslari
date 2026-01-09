# def ruyhat(mahsulot):
#     ruyxat = []
#     ruyxat.append(mahsulot)
#     return ruyxat

# print(ruyhat(mahsulot='olma'))

# def yosh_hisoblovchi(t_yil,h_yil=2025):
#     ruyxat = {}
#     ruyxat['yosh'] = h_yil-t_yil
#     ruyxat['voyaga yetgan'] = (h_yil-t_yil)>=18
#     return ruyxat

# print(yosh_hisoblovchi(t_yil=2020))

# try:
#     x = int(input("son k: "))
#     y = int(input("son k: "))
#     print(x/y)
# except ValueError:
#     print("int son kiriting.")
# except ZeroDivisionError:
#     print("Nolga bo'lib bo'lmaydi.")
# except Exception as e:
#     print(f"caught an error: {e}")

# davlatlar = {

# }
# davlatlar.get("ism", f"{key} topilmadi!")
# FUNCSIYA
# print()
# len()
# input()
# sum()
# max()
# min()

# def salom_beruvchi():
#     return "Assalomu Alaykum!"
# print(salom_beruvchi())

# def salom_beruvchi(ism):
#     return f"Assalomu Alaykum, {ism}"
# print(salom_beruvchi("Anvar"))

# def salom_beruvchi(ism="Anvar"):
#     return f"Assalomu Alaykum, {ism}"
# print(salom_beruvchi())

# print(salom_beruvchi())
# print(salom_beruvchi(ism="Anvar"))
# print(salom_beruvchi(ism="ali"))
# print(salom_beruvchi(ism="vali"))
# print(salom_beruvchi(ism="oysha"))
# print(salom_beruvchi(ism="aziz"))

# def katta_kichik(num1,num2):
#     if num1>=num2:
#         return num1
#     return num2

# print(katta_kichik(4,5))
# print(katta_kichik(num1=7, 9))
# print(katta_kichik(7,num2=58))
# print(katta_kichik(num2=56,num1=47))
# print(katta_kichik(num1=8,num2=1))

# list_ = [1,2,52,48,5,98]
# def custom_max(a):
#     if not a:
#         return "list bo'sh"
#     max_num = a[0]
#     for num in a:
#         if num > max_num:
#             max_num = num
#     return max_num

# print(custom_max(list_))

# def func_name(t_yil,h_yil=2025):
#     yosh = h_yil - t_yil
#     v_yetgan = yosh > 18
#     return dict(yosh=yosh, voyaga_yetgan=v_yetgan)

# print(func_name(2021))
# print(func_name(2003,2040))
# print(func_name(t_yil=2003,h_yil=2049))

