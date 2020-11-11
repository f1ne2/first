def transpose(self, A: List[List[int]]) -> List[List[int]]:
    transpose_matrix = []
    for i in range(len(A[0])):
        temp = []
        for j in range(len(A)):
            temp.append(A[j][i])
        transpose_matrix.append(temp)
    return transpose_matrix


def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
    temp = []
    if len(nums[0]) * len(nums) != r * c:
        return nums
    else:
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                temp.append(nums[i][j])
    new_matrix = []
    for k in range(r):
        new_matrix.append([0] * c)
    for b in range(r):
        for d in range(c):
            new_matrix[b][d] = temp.pop(0)
    return new_matrix


def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
    temp = []
    result = []
    for i in range(R):
        for j in range(C):
            temp.append([i, j, abs(i - r0) + abs(j - c0)])
    for a in sorted(temp, key=lambda x: (x[2])): result.append([a[0], a[1]])
    return result
