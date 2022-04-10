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
print("p = ", p)
print("q = ", q)

print("______________________________________________________")
q1_list = []
for z in range (1, p):
    if (z**q) % p == 1:
        q1_list.append(z)
print(q1_list)
g = max(q1_list)
print("g = ", g)

print("Работем в поле порядка p =", p)
x_array = []
for i in range (1, p//2):
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
a_array = []
for i in range (1, t):
    a_array.append(i)
print("D выбрал элементы многочлена a_i: ", a_array)

g_array = [g**K]
for i in range (1, t):
    g_array.append(g**i)
print(g_array)

arr = []
for x in x_array:
    total = 0
    for a in a_array:
        total += (a * (x**a))
        # print(total)
    total_fin1 = (K + total)
    total_fin = (total) % q
    # print(total_fin1)
    arr.append(total_fin)
    print("y[", x, "] = ", total_fin, "оправлено участнику P[", x, "]")
# print(arr)
# print(z_arr)

check = ((g**K) * (g**arr[0]) * (g**arr[1])**2) % q
print(check, g**arr[0]%p)
