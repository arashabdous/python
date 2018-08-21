# n = int(input())  # columns
# m = int(input())  # rows
# print(n, m)
# matrix = []
# for i in range(0, m):
#     matrix.append([])
#     for j in range(0, n):
#         matrix[i].append(0)
#         matrix[i][j] = int(input())
# print (matrix)

rows, cols = map(int, input('rows cols: ').split())
data = map(int, input('data: ').split())
mat = [*map(list, zip(*[data] * cols))]
print(rows, cols)
print(mat)
