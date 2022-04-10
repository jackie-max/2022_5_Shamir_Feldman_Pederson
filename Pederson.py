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

h = random.randint(1, p-1)
for i in range (h):
    if g**i % p == h:
        d = i
print(d)

K_init = bytes_to_long(b'secret')
K = K_init % p
print("Секретный ключ K = ", K)
t = 4
delta = K + random.randint(1, p-1)*z + random.randint(1, p-1)*z**2 + random.randint(1, p-1)*z**3
gamma = random.randint(1, p-1) + random.randint(1, p-1)*z + random.randint(1, p-1)*z**2 + random.randint(1, p-1)*z**3
print("gelta и gamma переданы участникам схемы")

for m in range (1, t-1):
    epsilon = g**delta[m] * h**gamma[m] %p
    print(epsilon)

u = []
w = []
for i in range (1, n):
    ui = u.append(delta[i])
    wi = w.append(gamma[i])

check = 0
for i in range (1, t):
    check *= epsilon[i]**i

if check == g**u[1]*h**w[1]:
    print("Протокол завершен успешно.")
else:
    print("Ошибка.")
    
