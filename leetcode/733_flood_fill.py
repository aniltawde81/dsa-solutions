image = [
    [1,1,1],
    [1,1,0],
    [1,0,1]
]

sr = 1
sc = 1
color = 2

original = image[sr][sc]

def dfs(r, c):
    if r < 0 or c < 0 or r >= len(image) or c >= len(image[0]):
        return

    if image[r][c] != original:
        return

    image[r][c] = color

    dfs(r + 1, c)
    dfs(r - 1, c)
    dfs(r, c + 1)
    dfs(r, c - 1)

if original != color:
    dfs(sr, sc)

print(image)
