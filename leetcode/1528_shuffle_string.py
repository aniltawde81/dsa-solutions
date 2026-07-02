s = "code"
indices = [3, 1, 2, 0]

result = [""] * len(s)

for i in range(len(s)):
    result[indices[i]] = s[i]

print("".join(result))
