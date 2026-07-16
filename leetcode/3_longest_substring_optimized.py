s = "abcabcbb"

left = 0
seen = {}
maximum = 0

for right in range(len(s)):
    if s[right] in seen and seen[s[right]] >= left:
        left = seen[s[right]] + 1

    seen[s[right]] = right
    maximum = max(maximum, right - left + 1)

print(maximum)
