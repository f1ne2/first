result = False
source = [0, 0]
blocked = [[0, 1],[1, 0]]
target = [0, 2]
D = []
Q = [source]
visited = [[]]
Qstart = 0
while Qstart < len(Q):
    u = Q[Qstart]
    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    for dir in dirs:
        neighbor = [Q[Qstart][0] + dir[0], Q[Qstart][1] + dir[1]]
        if neighbor not in blocked and neighbor not in visited:
            Q.append(neighbor)
        if neighbor == target:
            result = True
            break
    visited.append(Q[Qstart])
    Qstart += 1

print(result)
