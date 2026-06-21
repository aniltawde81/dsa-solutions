s = "(()())"

stack = []

for ch in s:
    if ch == "(":
        stack.append(ch)
    else:
        if stack:
            stack.pop()

if len(stack) == 0:
    print("Balanced")
else:
    print("Not Balanced")
