accounts = [
    [1, 2, 3],
    [3, 2, 1]
]

maximum = 0

for customer in accounts:
    wealth = sum(customer)
    if wealth > maximum:
        maximum = wealth

print(maximum)
