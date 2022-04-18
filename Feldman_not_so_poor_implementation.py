import random
from Crypto.Util.number import *
from Crypto.Random import get_random_bytes
import numpy

#Инициализация
p = getPrime(5)
q_list = []
for i in range (1, p):
    if (p-1) % i == 0:
        k = 0
        for j in range(2, i // 2 + 1):
            if (i % j == 0):
                k = k + 1
        if (k <= 0):
            q_list.append(i)

print(q_list)
q = max(q_list)
print("______________________________________________________")
print("p =", p)
print("q =", q)

print("______________________________________________________")
g_list = []
for i in range (1, p):
    if (i**q) % p == 1:
        g_list.append(i)
# print(g_list)
g = max(g_list)
print("g =", g)

print("Работем в поле порядка p =", p)
x_array = []
for i in range (1, 4):
    x_array.append(i)
print("D выбрал ненуленые элементы поля x_i: ", x_array)
n = len(x_array)
print("Число n выбранных ненулевых элементов поля:", n)
print("INFO: D передал элементы Pi")

K_init = bytes_to_long(b'secret')
K = K_init % p
print("Секретный ключ K = ", K)

#Распределение долей секрета
t = 3
print(t)
print("D выбрал t-1 =", t-1)
a_array = [g**K % p]
for i in range (1, t):
    a_array.append(i)
print("D выбрал элементы многочлена a_i: ", a_array)

y_array = []
for i in range (1, 4):
    y_array.append((a_array[2]*i**2 + a_array[1]*i + a_array[0]) % q)
print("Проверочные значения, переданные дилером участникам:", y_array)

#быстрая проверка, показывать лучше с ней

count = 0
for i in x_array:
    s = (g**y_array[i-1]) % p
    check = ((g ** a_array[0]) * ((g ** a_array[1]) ** i) * ((g ** a_array[2]) ** (i ** 2))) % p
    print(i, y_array[i-1], s, check)
    if check == s:
        print("Проверка", i, "-го пользователя прошла успешно.")
        count += 1
    else:
        print("Ошибка.")
        count = 0
if count == 3:
        print("Протокол завершен успешно.")
else:
        print("Ошибка.")

#полная проверка (для произвольного t)

# check_secret_array = []
# for i in range (1, t+1):
#     check = g ** a_array[0]
#     for k in range (1, t):
#         check *= (g**a_array[k])**(i**k)
#     check_fin = check % p
#     check_secret_array.append((check_fin))
#     print(check_fin)
# print("Массив для проверки:", check_secret_array)

# arr = []
# for x in x_array:
#     total = 0
#     for a in a_array:
#         total += (a * (x**a))
#         # print(total)
#     total_fin1 = (K + total)
#     total_fin = (total) % q
#     # print(total_fin1)
#     arr.append(total_fin)
#     print("y[", x, "] = ", total_fin, "оправлено участнику P[", x, "]")
# # print(arr)
# # print(z_arr)
#

# for i in range (0, t):
#     if (check_secret_array[i]) == (g**y_array[i]) % p:
#         print("Протокол завершен успешно.")
#     else:
#         print("Ошибка.")
