digits = [1, 2, 3]

number = int("".join(map(str, digits)))
number += 1

result = list(map(int, str(number)))

print(result)
