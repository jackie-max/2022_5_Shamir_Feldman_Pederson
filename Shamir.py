import random
from Crypto.Util.number import *
from Crypto.Random import get_random_bytes
import numpy

#Инициализация
p = getPrime(10)
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

print('___________________________________________________________________________________________________________________')
print('Вывод многочлена')

for i in range(1, t):
            print( "a[", i, "]", " * ", 'x', "^", i)
print('___________________________________________________________________________________________________________________')


arr = []
for x in x_array:
    total = 0
    for a in a_array:
        total += (a * (x**a))
        # print(total)
    total_fin = (K + total) %p
    arr.append(total_fin)
    print("y[", x, "] = ", total_fin, "оправлено участнику P[", x, "]")
print(arr)
# print(arr[5-1])

#Восстановление секрета
print('___________________________________________________________________________________________________________________')
print("Если вы хотите запустить восстановление секрета решением линейных уравнение, нажмите 1. Если вы хотите запустить восстановление секрета методом Лагранжа, нажмите 2.")
a = int(input())
# print(x_array[:t-1])
# print(x_array[:t-1][0])
# print(x_array[:t-1][1])
# print(x_array[:t-1][2])

if a == 1:
    matrix = []
    for i in range(t):
        massive = [1]
        for j in range(1, t):
            print("AAAAAAAAAAAAAAAAAAAAAA", i, x_array[:t][i])
            massive.append(((x_array[:t][i]) ** j))
        print(massive)
        matrix.append(massive)
    print(matrix)

    M2 = numpy.array(matrix)
    v2 = numpy.array(arr[:t])
    solve = numpy.linalg.solve(M2, v2) % p
    # print(solve[0])
    print("Восстановленный секрет:", round(solve[0]))
    # print(K)

    if (round(solve[0])) == K:
        print("Протокол завершен успешно.")
    else:
        print("Ошибка.")

X = x_array[:t]
Y = arr[:t]
print(X)
print(Y)


if a == 2:
    B1 = Y[0] * (X[1] / (X[1] - X[0])) * (X[2] / (X[2] - X[0])) + Y[1] * (X[0] / (X[0] - X[1])) * (
                X[2] / (X[2] - X[1])) + Y[2] * (X[1] / (X[1] - X[2])) * (X[0] / (X[0] - X[2]))

    print(B1 % p)
    if round(B1 % p) == K:
        print("Протокол завершен успешно.")
    else:
        print("Ошибка.")
