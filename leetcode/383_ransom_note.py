ransomNote = "aa"
magazine = "aab"

possible = True

for ch in ransomNote:
    if ch in magazine:
        magazine = magazine.replace(ch, "", 1)
    else:
        possible = False
        break

print(possible)
