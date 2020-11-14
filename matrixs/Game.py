# import only system from os
import os
# import sleep to show output for some time period
from time import sleep
from random import randint

# creation initial matrix
def original_matrix(w, h, dot):
    x = 0
    matrix1 = [[0] * h for i in range(w)]
    while x < dot:
        i, j = randint(0, w-1), randint(0, h-1)
        if matrix1[i][j] == 0:
            matrix1[i][j] = 1
            x += 1
    return matrix1

# computation of new matrix
def result_matrix(matrix):
    matrix_with_zero = [[0] * (len(matrix[0])+2) for k in range(len(matrix)+2)]
    for x in range(len(matrix)+2):
        for y in range(len(matrix[0])+2):
            if x == 0 or y == 0 or x == len(matrix)+1 or y == len(matrix[0])+1:
                matrix_with_zero[x][y] = 0
            else:
                matrix_with_zero[x][y] = matrix[x-1][y-1]
    new_matrix = [[0] * (len(matrix[0])+2) for k in range(len(matrix)+2)]
    for i in range(1, len(new_matrix)-1):
        for j in range(1, len(new_matrix[i])-1):
            sum = matrix_with_zero[i-1][j] + matrix_with_zero[i+1][j] + matrix_with_zero[i][j+1] + matrix_with_zero[i][j-1]\
                + matrix_with_zero[i-1][j-1] + matrix_with_zero[i+1][j+1] + matrix_with_zero[i-1][j+1] + matrix_with_zero[i+1][j-1]
            if matrix_with_zero[i][j] == 0 and sum != 3:
                new_matrix[i][j] = 0
            else:
                new_matrix[i][j] = 1
            if matrix_with_zero[i][j] == 1:
                if sum < 2 or sum > 3:
                    new_matrix[i][j] = 0
                else:
                    new_matrix[i][j] = 1
    result = [[0] * (len(new_matrix[0]) - 2) for k in range(len(new_matrix) - 2)]
    for k in range(1, len(new_matrix)-1):
        for q in range(1, len(new_matrix[0])-1):
            result[k-1][q-1] = new_matrix[k][q]
    return result

# initial data
rows = int(input("Rows of the matrix  "))
columns = int(input("Columns of the matrix  "))
alive_dots = int(input("Alive dots  "))
# initial array
matrix = original_matrix(rows, columns, alive_dots)
# outputting arrays
while True:
    sleep(2)
    os.system("cls")
    matrix = result_matrix(matrix)
    for i in range(len(matrix)):
        print(matrix[i])
        if i == len(matrix)-1:
            print("\n")

