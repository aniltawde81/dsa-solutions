items = [
    ["phone", "blue", "pixel"],
    ["computer", "silver", "lenovo"],
    ["phone", "gold", "iphone"]
]

ruleKey = "color"
ruleValue = "silver"

index = {
    "type": 0,
    "color": 1,
    "name": 2
}

count = 0

for item in items:
    if item[index[ruleKey]] == ruleValue:
        count += 1

print(count)
