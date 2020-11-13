# import only system from os
import os
# import sleep to show output for some time period
from time import sleep

from random import randint

# создание исходной матрицы по заданным параметрам
def original_matrix(a,b,dot):
    x = set()
    matrix1 = [[0] * b for i in range(a)]
    for t in range(dot):
        i,j = randint(0,a-1),randint(0,b-1)
        string = str(i) + str(j)
        print(string)
        if string not in x:
            x.add(string)
            matrix1[i][j] = 1
        else:
            t -= 1
            print(t)
    print(x)
    return matrix1

# Вычисление новой матрицы
def result_matrix(a,b,matrix):
    result = []
    matrix_with_zero = [[0] * (b+2) for k in range(a+2)]
    for x in range(a+2):
        for y in range(b+2):
            if x == 0 or y == 0 or x == a+1 or y == b+1:
                matrix_with_zero[x][y] = 0
            else:
                matrix_with_zero[x][y] = matrix[x - 1][y - 1]
    zero_matrix = [[0] * (b+2) for k in range(a+2)]
    for i in range(1, len(zero_matrix)-1):
        for j in range(1, len(zero_matrix[i])-1):
            sum = matrix_with_zero[i-1][j] + matrix_with_zero[i+1][j] + matrix_with_zero[i][j+1] + matrix_with_zero[i][j-1]\
            + matrix_with_zero[i-1][j-1] + matrix_with_zero[i+1][j+1] + matrix_with_zero[i-1][j+1] + matrix_with_zero[i+1][j-1]
            if matrix_with_zero[i][j] == 0:
                if sum != 3:
                    zero_matrix[i][j] = 0
                else:
                    zero_matrix[i][j] = 1
            if matrix_with_zero[i][j] == 1:
                if sum < 2 or sum > 3:
                    zero_matrix[i][j] = 0
                else:
                    zero_matrix[i][j] = 1
    for k in range(1,len(zero_matrix)-1):
        del zero_matrix[k][0]
        del zero_matrix[k][len(zero_matrix[k])-1]
    result = zero_matrix[1:len(zero_matrix)-1]
    return result

# исходные данные по размерам поля и числу шагов
r = int(input("Введите число строк поля"))
c = int(input("Введите число столбцов поля"))
alive_dot = int(input("Введите число живых точек"))
# исходный массив игры
m1 = original_matrix(r,c,alive_dot)
print(m1)
# выходные массивы игры
g = 0
while g == 0:
    sleep(2)
    os.system("cls")
    m1 = result_matrix(r,c,m1)
    print(m1)

