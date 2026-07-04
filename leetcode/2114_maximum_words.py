sentences = [
    "alice and bob love leetcode",
    "i think so too",
    "this is great thanks very much"
]

maximum = 0

for sentence in sentences:
    words = len(sentence.split())
    if words > maximum:
        maximum = words

print(maximum)
