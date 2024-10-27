matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

for i in range(len(matrix[0])):
    print(' '.join(str(matrix[j][i]) for j in range(len(matrix))))