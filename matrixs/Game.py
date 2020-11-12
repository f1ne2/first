# Вычисление новой матрицы
def result_matrix(m1):
    for i in range(1,len(m2)-1):
        for j in range(1,len(m2[i])-1):
            sum = m1[i-1][j] + m1[i+1][j] + m1[i][j+1] + m1[i][j-1]\
            + m1[i-1][j-1] + m1[i+1][j+1] + m1[i-1][j+1] + m1[i+1][j-1]
            print(sum)
            if m1[i][j] == 0:
                if sum != 3:
                    m2[i][j] = 0
                else:
                    m2[i][j] = 1
            if m1[i][j] == 1:
                if sum < 2 or sum > 3:
                    m2[i][j] = 0
                else:
                    m2[i][j] = 1
    return m2
# исходные данные по размерам поля и числу шагов
m1 = [[0,0,0,0,0,0,0],[0,0,1,1,1,0,0],[0,0,1,0,0,0,0],[0,0,0,0,1,0,0],[0,0,0,0,0,0,0]]
m2 = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
steps = 2
# исходный массив игры
print(m1)
# выходной массив игры
m2 = result_matrix(m1)
if steps >= 2:
    for k in range(1,steps):
        m2 = result_matrix(m2)
print(m2)

