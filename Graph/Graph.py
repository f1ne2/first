from random import randint


# creation initial matrix
def original_matrix(w, h, dot):
    x = 0
    goal = []
    start_point = []
    matrix1 = [[0] * h for i in range(w)]
    while x < dot:
        i, j = randint(0, w - 1), randint(0, h - 1)
        if matrix1[i][j] == 0:
            matrix1[i][j] = 1
            x += 1
    while x < dot + 1:
        i, j = randint(0, w - 1), randint(0, h - 1)
        if matrix1[i][j] == 0 and goal == []:
            goal.append(i)
            goal.append(j)
        if matrix1[i][j] == 0 and goal != [] and goal[0] != i and goal[1] != j:
            start_point.append(i)
            start_point.append(j)
            x += 1
    return matrix1, goal, start_point


def computation(matrix2, start_point, goal):
    output = False
    Q = [start_point]
    visited = []
    Qstart = 0
    distance = []
    distance.append(0)
    u = 0
    way = []
    while Qstart < len(Q) and output != True:
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for dir in dirs:
            neighbor = [Q[Qstart][0] + dir[0], Q[Qstart][1] + dir[1]]
            if neighbor[0] < 0 or neighbor[1] < 0 or neighbor[0] > len(matrix2) - 1 or neighbor[1] > len(
                    matrix2[0]) - 1:
                continue
            if neighbor == goal:
                output = True
                break
            if neighbor not in visited and matrix2[neighbor[0]][neighbor[1]] != 1:
                Q.append(neighbor)
                u = distance[Qstart]
                distance.append(u + 1)
        visited.append(Q[Qstart])
        Qstart += 1
    for i in range(len(visited)):
        if i != len(visited) - 1 and distance[i + 1] > distance[i]:
            way.append(visited[i])
    way.append(visited[-1])
    way.append(target)
    return output, way


# initial data
rows = int(input("Rows of the matrix  "))
columns = int(input("Columns of the matrix  "))
alive_dots = int(input("Alive dots  "))
# initial array
matrix, target, source = original_matrix(rows, columns, alive_dots)
for i in range(len(matrix)):
    print(matrix[i])
    if i == len(matrix) - 1:
        print("\n")
print("source", source, "\t", "target", target)
# outputting data
result, path = computation(matrix, source, target)
if result == True:
    print(result, "\n", path)
else:
    print(result)
