a = 12
b = 18

temp_a = a
temp_b = b

while temp_b:
    temp_a, temp_b = temp_b, temp_a % temp_b

gcd = temp_a

lcm = (a * b) // gcd

print(lcm)
