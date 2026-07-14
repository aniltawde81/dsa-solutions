from collections import defaultdict

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

groups = defaultdict(list)

for word in strs:
    key = "".join(sorted(word))
    groups[key].append(word)

print(list(groups.values()))
