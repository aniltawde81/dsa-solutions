mapping = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}

digits = "23"

result = []

def backtrack(index, path):
    if len(path) == len(digits):
        result.append(path)
        return

    for ch in mapping[digits[index]]:
        backtrack(index + 1, path + ch)

if digits:
    backtrack(0, "")

print(result)
