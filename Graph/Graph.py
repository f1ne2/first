class Stack :
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return (self.items == [])

result = False
source = [0, 0]
blocked = [[0, 10], [1, 11]]
target = [5, 25]
queue = Stack()
matrix = [[0] * 100 for k in range(100)]
queue.push(source)
dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
visited = []
u = []
while not queue.is_empty() and result != True:
    u = (queue.pop())
    print(u)
    for dir in dirs:
        neighbor = [u[0] + dir[0], u[1] + dir[1]]
        if neighbor[0] < 0 or neighbor[1] < 0 or neighbor[0] > len(matrix) - 1 or neighbor[1] > len(matrix) - 1:
            print(1)
            continue
        if neighbor == target:
            result = True
            break
        if neighbor not in blocked and neighbor not in visited:
            queue.push(neighbor)
            print(2)
    visited.append(u)
    u.clear()

print(result)
