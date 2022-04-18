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
for i in range (1, 4):
    x_array.append(i)
print("D выбрал ненуленые элементы поля x_i: ", x_array)
n = len(x_array)
print("Число n выбранных ненулевых элементов поля:", n)
print("INFO: D передал элементы Pi")

d = getPrime(4)

h = g**d % p
print("Открытое общедоступное число: ", h)
print("Закрытое общедоступное число: ", d)

K_init = bytes_to_long(b'secret')
K = K_init % p
print("Секретный ключ K = ", K)
t = 3

delta_array = []
for i in range (1, t+1):
    delta_array.append(i)
print("D выбрал элементы многочлена delta: ", delta_array)

gamma_array = []
for i in range (1, t+1):
    gamma_array.append(i+1)
print("D выбрал элементы многочлена gamma: ", gamma_array)
# delta = K + random.randint(1, p-1)*z + random.randint(1, p-1)*z**2 + random.randint(1, p-1)*z**3
# gamma = random.randint(1, p-1) + random.randint(1, p-1)*z + random.randint(1, p-1)*z**2 + random.randint(1, p-1)*z**3
print("gelta и gamma переданы участникам схемы")

epsilon_array = []
for i in range (1, t+1):
    epsilon_array.append(((g**delta_array[i-1])*(h**gamma_array[i-1])) % p)
print("Проверочные значения, переданные дилером участникам:", epsilon_array)

delta = []
gamma = []
for i in range (1, 4):
    delta.append((delta_array[2]*i**2 + delta_array[1]*i + delta_array[0]) % q)
    gamma.append((gamma_array[2]*i**2 + gamma_array[1]*i + gamma_array[0]) % q)
print("Проверочные значения, переданные дилером участникам:", delta, gamma)

#быстрая проверка, показывать лучше с ней

u = delta_array
w = gamma_array
count = 0
for i in range (1, t+1):
    s = (g**delta[i-1])*(h**gamma[i-1]) % p
    check = ((epsilon_array[0]) * ((epsilon_array[1]) ** i) * ((epsilon_array[2]) ** (i ** 2))) % p
    print(i, s, check)
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
#     check = epsilon_array[0]
#     for k in range (1, t):
#         check *= (epsilon_array[k])**(i**k)
#     check_fin = check % p
#     check_secret_array.append((check_fin))
#     print(check_fin)
# print("Массив для проверки:", check_secret_array)


# for i in range (1, n):
#     ui = u.append(delta_array[i])
#     wi = w.append(gamma_array[i])
#
# check = 0
# for i in range (1, t):
#     check *= epsilon_array[i-1]**i

# for i in range (0, t):
#     if (check_secret_array[i]) == (g**delta[i])*(h**gamma[i]) % p:
#         print("Протокол завершен успешно.")
#     else:
#         print("Ошибка.")
