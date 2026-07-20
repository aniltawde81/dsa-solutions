mat = [
    [1, 2],
    [3, 4]
]

r = 1
c = 4

flat = []

for row in mat:
    for num in row:
        flat.append(num)

result = []

index = 0
for i in range(r):
    new_row = []
    for j in range(c):
        new_row.append(flat[index])
        index += 1
    result.append(new_row)

print(result)
