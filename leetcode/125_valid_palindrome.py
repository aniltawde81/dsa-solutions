s = "A man, a plan, a canal: Panama"

text = ""

for ch in s:
    if ch.isalnum():
        text += ch.lower()

if text == text[::-1]:
    print(True)
else:
    print(False)
