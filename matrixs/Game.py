from random import randint

# создание рандомного массива
def original_matrix(a,b):
    m1 = []
    for i in range(a+2):
        m2 = []
        for j in range(b+2):
            if i == 0 or i == a+1 or j == 0 or j == b+1:
                m2.append(0)
            else:
                m2.append(randint(0,1))
        m1.append(m2)
    return m1

# Добавление нулей в новую матрицу
def zero_matrix(a,b):
    m1 = []
    for i in range(a+2):
        m2 = []
        for j in range(b+2):
            m2.append(0)
        m1.append(m2)
    return m1

# Вычисление новой матрицы
def result_matrix(m1,steps,a,b):
    m4 = zero_matrix(a,b)
    for i in range(1,a+1):
        for j in range(1,b+1):
            sum = m1[i-1][j] + m1[i+1][j] + m1[i][j+1] + m1[i][j-1]\
            + m1[i-1][j-1] + m1[i+1][j+1] + m1[i-1][j+1] + m1[i+1][j-1]
            if sum < 2 or sum > 3:
                m4[i][j] = 0
            if sum == 2 or sum == 3:
                m4[i][j] = 1
    return m4

# исходные данные по размерам поля и числу шагов
r = 3
c = 3
steps = 2
# исходный массив игры
m1 = original_matrix(r,c)
print(m1)
# выходной массив игры
m2 = result_matrix(m1,steps,r,c)
if steps >= 2:
    for k in range(1,steps):
        m2 = result_matrix(m2,steps-1,r,c)
print(m2)

