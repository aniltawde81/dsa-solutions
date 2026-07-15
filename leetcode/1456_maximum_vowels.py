s = "abciiidef"
k = 3

vowels = "aeiou"

count = 0

for ch in s[:k]:
    if ch in vowels:
        count += 1

maximum = count

for i in range(k, len(s)):
    if s[i] in vowels:
        count += 1
    if s[i - k] in vowels:
        count -= 1

    maximum = max(maximum, count)

print(maximum)
