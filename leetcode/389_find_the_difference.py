s = "abcd"
t = "abcde"

for ch in t:
    if t.count(ch) != s.count(ch):
        print(ch)
        break
