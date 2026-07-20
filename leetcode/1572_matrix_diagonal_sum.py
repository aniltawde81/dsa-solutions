mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

n = len(mat)
total = 0

for i in range(n):
    total += mat[i][i]
    if i != n - 1 - i:
        total += mat[i][n - 1 - i]

print(total)
